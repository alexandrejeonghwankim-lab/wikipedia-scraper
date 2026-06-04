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
import re
import json

class WikipediaScraper:
	"""
	Class responsible for downloading and parsing HTML documents.

	Attributes:
		session: (requests.Session) passed down from the parent application context.
	"""

	def __init__(self, session: requests.Session) -> None:
		"""
		Constructor for a WikipediaScraper.

		Params:
			self: (requests.Session) Number of tables in the openspace.
		Return: 
			None.
		"""
		self.session = session
		self.leaders = {}

	def fetch_html(self, url: str) -> str:
		"""
		This function requests raw HTML text from the given URL.

		Params:
			url: (str) The Wikipedia page URL.
		Return:
			req.text: (str) The raw HTML text.
		"""

		try:
			req = self.session.get(url, headers={"User-Agent": "Mozilla/5.0"})
			req.raise_for_status()
			return req.text
		except requests.exceptions.ConnectionError as error:
			print("Connection error occurred:", error)
		except requests.exceptions.HTTPError as error:
			print("HTTP error occurred:", error)
		except requests.exceptions.Timeout as error:
			print("Timeout Error")
		except requests.exceptions.RequestException as error:
			print("Request error")
		return None

	def get_first_paragraph(self, html: str) -> str:
		"""
		This function parses the raw HTML and returns the first paragraph.

		Params:
			html: (str) Source raw HTML.
		Return:
			first_paragraph: (str) Extracted first paragraph.
		"""
		if html is None:
			return None
		soup = BeautifulSoup(html, "html.parser")
		paragraphs = soup.find_all("p")
		first_paragraph = ""
		for paragraph in paragraphs:
			if paragraph.find("b"):
				first_paragraph = paragraph.get_text()
				break
		return first_paragraph

	def clean_text(self, text: str) -> str:
		"""
		This function strips the first paragraph from unwanted elements,
		such as extra whitespaces and unwanted characters. 

		Params:
			text: (str) The extracted first paragraph.
		Return:
			text: (str) The cleaned first paragraph.
		"""
		while re.search(r"\[[^\[\]]*\]", text): # Removes everything in [], including nested
			text = re.sub(r"\[[^\[\]]*\]", "", text)
		text = re.sub(r"\s+", " ", text) # Reduces multiple white spaces to single space
		text  = re.sub(r"ⓘ", "", text) # Removes ⓘ
		text  = re.sub(r"\bÉcouter\b\s*", "", text) # Removes "Écouter" in the French page
		text  = re.sub(r"\(\s*French:\s*; ", "(", text) # Removes "French: ;" in the English page
		return text 

	def to_json_file(self, filepath: str) -> None:
		with open(filepath, "w", encoding="UTF-8") as file:
			json.dump(self.leaders, file, ensure_ascii=False, indent=4)
