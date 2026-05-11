import argparse
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional

import requests
from bs4 import BeautifulSoup

BASE = Path(__file__).parent
OUT_DIR = BASE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_html(source: str) -> str:
    if source.startswith("http://") or source.startswith("https://"):
        resp = requests.get(source, timeout=20)
        resp.raise_for_status()
        return resp.text
    return Path(source).read_text(encoding="utf-8")


def parse_rating(text: str) -> Optional[float]:
    if not text:
        return None
    match = re.search(r"([0-9]+(\.[0-9]+)?)", text)
    if not match:
        return None
    return float(match.group(1))


def extract_jsonld_reviews(soup: BeautifulSoup) -> List[Dict[str, Any]]:
    reviews = []
    scripts = soup.find_all("script", attrs={"type": "application/ld+json"})
    for s in scripts:
        raw = s.string or ""
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue

        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict):
                continue
            revs = item.get("review")
            if not revs:
                continue
            if isinstance(revs, dict):
                revs = [revs]

            for r in revs:
                if not isinstance(r, dict):
                    continue
                author = r.get("author")
                if isinstance(author, dict):
                    author = author.get("name")
                rating = r.get("reviewRating")
                if isinstance(rating, dict):
                    rating = rating.get("ratingValue")

                reviews.append({
                    "customer_name": author or "",
                    "rating": parse_rating(str(rating)) if rating else None,
                    "comment_title": r.get("name", ""),
                    "comment": r.get("reviewBody", ""),
                    "comment_tags": [],
                    "date": r.get("datePublished", "")
                })

    return reviews


def extract_with_selectors(soup: BeautifulSoup, config: dict) -> List[Dict[str, Any]]:
    reviews = []
    blocks = soup.select(config.get("review_block", ""))
    for block in blocks:
        name = block.select_one(config.get("reviewer", ""))
        rating = block.select_one(config.get("rating", ""))
        title = block.select_one(config.get("title", ""))
        body = block.select_one(config.get("body", ""))
        date = block.select_one(config.get("date", ""))
        tags = block.select(config.get("tags", ""))

        reviews.append({
            "customer_name": name.get_text(strip=True) if name else "",
            "rating": parse_rating(rating.get_text(strip=True)) if rating else None,
            "comment_title": title.get_text(strip=True) if title else "",
            "comment": body.get_text(strip=True) if body else "",
            "comment_tags": [t.get_text(strip=True) for t in tags] if tags else [],
            "date": date.get_text(strip=True) if date else ""
        })

    return reviews


def save_outputs(reviews: List[Dict[str, Any]]) -> None:
    json_path = OUT_DIR / "reviews.json"
    csv_path = OUT_DIR / "reviews.csv"

    json_path.write_text(json.dumps(reviews, indent=2), encoding="utf-8")

    if reviews:
        headers = list(reviews[0].keys())
        lines = [",".join(headers)]
        for r in reviews:
            row = []
            for h in headers:
                value = r.get(h, "")
                if isinstance(value, list):
                    value = "|".join(value)
                value = str(value).replace("\n", " ").replace(",", " ")
                row.append(value)
            lines.append(",".join(row))
        csv_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="URL or local HTML file")
    parser.add_argument("--config", default=str(BASE / "config.json"))
    args = parser.parse_args()

    html = load_html(args.source)
    soup = BeautifulSoup(html, "html.parser")

    reviews = extract_jsonld_reviews(soup)
    if not reviews:
        config = json.loads(Path(args.config).read_text(encoding="utf-8"))
        reviews = extract_with_selectors(soup, config)

    save_outputs(reviews)
    print(f"Saved {len(reviews)} reviews to {OUT_DIR}")


if __name__ == "__main__":
    main()
