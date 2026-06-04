# Track 2: The HTML Scraper (src/html_scraper.py)

# Build a WikipediaScraper class responsible only for downloading and parsing HTML documents.
# Attributes: session (passed down from the parent application context).
# Methods:
# fetch_html(url: str): Safely requests raw HTML text. Must include robust exception handling to deal with 404s, 500s, or connection drops.
# get_first_paragraph(html: str): Parses raw HTML with BeautifulSoup, finds the first true biographical narrative paragraph (
# ), and returns it.

# clean_text(text: str): A cleaning utility method to strip out unwanted characters, whitespace, or Wikipedia citation brackets (e.g., [1], [citation needed]).
# to_json_file(filepath: str) -> None stores the data structure into a JSON file

import requests
from bs4 import BeautifulSoup

class WikipediaScraper:
	"""
	Class responsible for downloading and parsing HTML documents.

	Attributes:
		session: (???) passed down from the parent application context.
	"""

	def __init__(self, session) -> None:
		self.session = session

	def fetch_html(self, url):
		"""
		This function requests raw HTML text from the given URL.

		Params:
			url: (str) Wikipedia page URL.
		Return:
			None.
		"""

		try:
			req = self.session.get(url, headers={"User-Agent": "Mozilla/5.0"})
			req.raise_for_status()
		except requests.exceptions.ConnectionError as error:
			print("Connection error occurred:", error)
		except requests.exceptions.HTTPError as error:
			print("HTTP error occurred:", error)


	def get_first_paragraph(html):
		"""
		This function parses the raw HTML and returns the first paragraph.

		Params:
			html: (str) Source raw HTML.
		Return:
			first_paragraph: (str) Extracted first paragraph.
		"""
		soup = BeautifulSoup(req.text, "html.parser")
		paragraphs = soup.find_all("p")
		first_paragraph = {}
		for paragraph in paragraphs:
			if paragraph.find("b"):
				first_paragraph = paragraph.get_text()
				break

	def clean_text(text):
		pass

	def to_json_file(filepath):
		pass
