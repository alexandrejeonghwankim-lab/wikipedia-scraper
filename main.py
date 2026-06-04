from src.api_client import CountryLeadersAPI
from src.html_scraper import WikipediaScraper
import requests

# API Setup
# Build countries

# WikipediaScraper Setup
wiki_session = requests.Session() # Launches session
wiki_session.headers.update({"User-Agent": "Mozilla/5.0"})
scraper = WikipediaScraper(wiki_session)
leaders_per_country = {} # Placeholder for final structure

# Scraping
for country in countries:
	leaders = [] # Placeholder for leaders list (get from get_leaders)
	leaders_per_country[country] = leaders
	for leader in leaders:
		wiki_url = "" # build url - API part? 
		html = scraper.fetch_html(wiki_url)
		first_paragraph = scraper.get_first_paragraph(html)
		clean_paragraph = scraper.clean_text(first_paragraph)
		leader["first_paragraph"] = clean_paragraph

# Saving to .json
scraper.leaders = leaders_per_country
scraper.to_json_file("leaders.json")