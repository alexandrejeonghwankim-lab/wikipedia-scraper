# Track 2: The HTML Scraper (src/html_scraper.py)

# Build a WikipediaScraper class responsible only for downloading and parsing HTML documents.
# Attributes: session (passed down from the parent application context).
# Methods:
# fetch_html(url: str): Safely requests raw HTML text. Must include robust exception handling to deal with 404s, 500s, or connection drops.
# get_first_paragraph(html: str): Parses raw HTML with BeautifulSoup, finds the first true biographical narrative paragraph (
# ), and returns it.

# clean_text(text: str): A cleaning utility method to strip out unwanted characters, whitespace, or Wikipedia citation brackets (e.g., [1], [citation needed]).
# to_json_file(filepath: str) -> None stores the data structure into a JSON file

