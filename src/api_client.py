# Track 1: The API Client (src/api_client.py)

# Build a CountryLeadersAPI class responsible only for communicating with the REST API.
# Attributes: base_url, country_endpoint, leaders_endpoint, cookies_endpoint, and session (optional: utilizing a persistent requests.Session()).
# Methods:
# refresh_cookie(): Checks validity and refreshes the session cookie when expired.
# get_countries(): Queries the API and returns a clean list of supported country codes.
# get_leaders(country: str): Fetches and returns the raw JSON list of leaders for a targeted country.

class CountyLeadersAPI:
    """Class responsible only for communicating with the REST API"""
    def __init__(self, 
                 base_url = "https://country-leaders.onrender.com", 
                 country_endpoint, 
                 leaders_endpoint, 
                 cookies_endpoint, 
                 session):
        self.base_url = base_url
        self.country_endpoint = 
    
    def refresh_cookie():
        pass

    def get_countries():
        pass

    def get_leaders(country: str):
        pass