# Track 1: The API Client (src/api_client.py)

# Build a CountryLeadersAPI class responsible only for communicating with the REST API.
# Attributes: base_url, country_endpoint, leaders_endpoint, cookies_endpoint, and session (optional: utilizing a persistent requests.Session()).
# Methods:
# refresh_cookie(): Checks validity and refreshes the session cookie when expired.
# get_countries(): Queries the API and returns a clean list of supported country codes.
# get_leaders(country: str): Fetches and returns the raw JSON list of leaders for a targeted country.

import requests

class CountryLeadersAPI:
    """Class responsible only for communicating with the REST API"""
    def __init__(self):
        
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.session = requests.Session()
    
    def refresh_cookie(self):
        response = self.session.get(self.base_url + self.cookies_endpoint)
        return response.cookies


    def get_countries(self):
        url = self.base_url + self.country_endpoint
        cookies = self.refresh_cookie()
        response = self.session.get(url, cookies = cookies)
        countries = response.json()
        return countries

        

    def get_leaders(self,country: str):
        url = self.base_url + self.leaders_endpoint + "?country=" + country
        cookies = self.refresh_cookie()
        response = self.session.get(url, cookies = cookies)
        leaders = response.json()
        return leaders 