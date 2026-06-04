# Track 1: The API Client (src/api_client.py)

# Build a CountryLeadersAPI class responsible only for communicating with the REST API.
# Attributes: base_url, country_endpoint, leaders_endpoint, cookies_endpoint, and session (optional: utilizing a persistent requests.Session()).
# Methods:
# refresh_cookie(): Checks validity and refreshes the session cookie when expired.
# get_countries(): Queries the API and returns a clean list of supported country codes.
# get_leaders(country: str): Fetches and returns the raw JSON list of leaders for a targeted country.

import requests

class CountryLeadersAPI:
    """
    This class handles all API communications such as retrieving countries,
    leaders, and managing session cookie
    """
    def __init__(self):
        """Initialize the API client..
        
        Sets the base URL, API endpoints, and creates a session
        for making HTTP requests efficiently.
        """    
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.session = requests.Session()
    
    def refresh_cookie(self):
        """
        Refresh the session cookies.

        Sends a request to the cookie endpoint and returns the updated cookies.
        """
        response = self.session.get(self.base_url + self.cookies_endpoint)
        return response.cookies


    def get_countries(self):
        """
        Retrieve the list of available country codes.

        Returns:
        list: A list of country codes from the API.
        """
        url = self.base_url + self.country_endpoint
        cookies = self.refresh_cookie()
        response = self.session.get(url, cookies = cookies)
        countries = response.json()
        return countries

        

    def get_leaders(self,country: str):
        """
        Retrieve leaders for a given country.

        Args:
        country (str): The country code.

        Returns:
        list: A list of leaders for the specified country.
        """
        url = self.base_url + self.leaders_endpoint + "?country=" + str(country)
        cookies = self.refresh_cookie()
        response = self.session.get(url, cookies = cookies)
        leaders = response.json()
        return leaders 