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
		session: (requests.Session) Passed down from the parent application context.
		leaders: (dict) Contains leaders grouped by country.
	"""

	def __init__(self, session: requests.Session) -> None:
		"""
		Constructor for a WikipediaScraper.

		Params:
			session: (requests.Session) Passed down from the parent application context.
		Return: 
			None.
		"""
		self.session = session
		self.leaders = {}

	def fetch_html(self, url: str) -> str | None:
		"""
		This function requests raw HTML text from the given URL.
		In case of error, it will catch the corresponding exception,
		and prints an error message.

		Params:
			url: (str) The Wikipedia page URL.
		Return:
			req.text: (str) The raw HTML text if request is successful.
			None: If request is unsuccessful.
		"""

		try:
			req = self.session.get(url, headers={"User-Agent": "Mozilla/5.0"})
			req.raise_for_status()
			return req.text # Return when request is successful
		except requests.exceptions.ConnectionError as error:
			print("Connection error occurred:", error)
		except requests.exceptions.HTTPError as error:
			print("HTTP error occurred:", error)
		except requests.exceptions.Timeout as error:
			print("Timeout Error")
		except requests.exceptions.RequestException as error:
			print("Request error")
		return None # Return when error

	def get_first_paragraph(self, html: str) -> str | None:
		"""
		This function parses the raw HTML and returns the first paragraph.

		Params:
			html: (str) Source raw HTML.
		Return:
			first_paragraph: (str) Extracted first paragraph.
		"""
		if html is None: # If html is empty, return None
			return None
		soup = BeautifulSoup(html, "html.parser")
		paragraphs = soup.find_all("p") # Find all paragraphs
		first_paragraph = ""
		for paragraph in paragraphs: # Look for the first paragraph with a bolded element
			if paragraph.find("b"):
				first_paragraph = paragraph.get_text()
				break
		return first_paragraph

	def clean_text(self, text: str) -> str | None:
		"""
		This function strips the first paragraph from unwanted elements,
		such as extra whitespaces and unwanted characters. 

		Params:
			text: (str) The extracted first paragraph.
		Return:
			text: (str) The cleaned first paragraph.
			None: If text was empty.
		"""

		if text is None: # If there is no text, return None
			return None
		text = re.sub(r"\(.*?\)", "", text)
		text = re.sub(r"\[.*?\]", "", text)
		text = re.sub(" +", " ", text)
		text = re.sub(" +", " ", text)
		text = re.sub(r"ⓘ", "", text)
		text = re.sub(r"Écouter", "", text)
		text = re.sub(r"\s{2,}", " ", text)
		return text 

	def to_json_file(self, filepath: str) -> None:
		"""
		This function prints the scraping result into a .json file. 

		Params:
			filepath: (str) The .json filename.
		Return:
			None.
		"""
		with open(filepath, "w", encoding="UTF-8") as file:
			json.dump(self.leaders, file, ensure_ascii=False, indent=4)
