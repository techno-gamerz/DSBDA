# Assignment Group C1: Web Review Scraper

## 1. Problem Statement
Design and implement a Python-based web scraper to extract customer reviews, ratings, comments, and tags from an e-commerce product page. The scraper should be flexible enough to handle both structured JSON-LD data and unstructured HTML using CSS selectors.

## 2. Objectives
- To understand the principles of web scraping using Python.
- To learn how to parse HTML documents using BeautifulSoup.
- To handle different data formats (JSON-LD vs. CSS selectors).
- To export scraped data into structured formats like JSON and CSV.

## 3. Prerequisites
- Python 3.9 or higher
- Libraries: `requests`, `beautifulsoup4`
- Basic knowledge of HTML structure and CSS selectors.

## 4. Implementation Details
The implementation consists of the following components:
- **`scrape_reviews.py`**: The core script that fetches HTML (from a URL or local file) and extracts review data.
- **`config.json`**: A configuration file containing CSS selectors for specific page elements (reviewer name, rating, body, etc.).
- **`data/sample_product_page.html`**: A mock e-commerce page for demonstration and safe testing.
- **`outputs/`**: Directory where the extracted data is stored in `reviews.json` and `reviews.csv`.

### Key Functions:
- `load_html()`: Handles fetching content from a URL or reading a local file.
- `extract_jsonld_reviews()`: Attempts to find `application/ld+json` scripts which often contain structured review data (Schema.org).
- `extract_with_selectors()`: Fallback method using CSS selectors from the config file.
- `save_outputs()`: Formats and writes the data to disk.

## 5. Execution Instructions
1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run on Sample Data**:
   ```bash
   python scrape_reviews.py --source data/sample_product_page.html
   ```
4. **Run on Live URL** (where permitted):
   ```bash
   python scrape_reviews.py --source "https://example.com/product"
   ```
For a real website, update `config.json` selectors if JSON-LD review data is not available. Respect the website terms of service and robots policy.

## 6. Result Analysis
The script successfully identifies review blocks and extracts:
- **Customer Name**: The identity of the reviewer.
- **Rating**: Numerical score (parsed using regex).
- **Comment/Body**: The text content of the review.
- **Tags**: Specific keywords associated with the review.
- **Date**: The publication date.

The output is provided in both JSON (for programmatic use) and CSV (for spreadsheet analysis).
