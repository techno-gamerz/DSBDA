# Group C1 - Review scraper (Python)

Aim
- Scrape comments, reviews, ratings, tags, and customer names from an ecommerce page.

Tools and environment
- Python 3.9+
- requests, beautifulsoup4

Files
- scrape_reviews.py
- config.json
- data/sample_product_page.html
- requirements.txt

Steps
1. Install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run on the local sample HTML (safe demo):
   ```bash
   python scrape_reviews.py --source data/sample_product_page.html
   ```
3. Run on a real page (only where you have permission):
   ```bash
   python scrape_reviews.py --source "https://example.com/product-page"
   ```
4. If JSON-LD reviews are not present, update config.json with CSS selectors that match the page.
5. Check outputs in outputs/.

Outputs
- outputs/reviews.json
- outputs/reviews.csv

Notes
- Prefer pages that expose JSON-LD (script type application/ld+json) for stable extraction.
- Always respect robots.txt and site terms of service.
