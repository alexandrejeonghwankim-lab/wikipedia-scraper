from src.api_client import CountryLeadersAPI
from src.html_scraper import WikipediaScraper
import requests

# API Setup
api = CountryLeadersAPI()
# Build countries
countries = api.get_countries()

# WikipediaScraper Setup
wiki_session = requests.Session() # Launches session.
wiki_session.headers.update({"User-Agent": "Mozilla/5.0"})
scraper = WikipediaScraper(wiki_session)
leaders_per_country = {} # Placeholder for final structure.

# Scraping
# For each country, get its leaders.
for country in countries:
	leaders = api.get_leaders(country)
	leaders_per_country[country] = leaders
# For each leader, get the wikipedia url, extracts and cleans the first paragraph of the page.
	for leader in leaders:
		wiki_url = leader["wikipedia_url"]
		html = scraper.fetch_html(wiki_url)
		first_paragraph = scraper.get_first_paragraph(html)
		clean_paragraph = scraper.clean_text(first_paragraph)
		leader["first_paragraph"] = clean_paragraph

# Saving to .json
scraper.leaders = leaders_per_country
scraper.to_json_file("leaders.json")