# Track 1: The API Client (src/api_client.py)

# Build a CountryLeadersAPI class responsible only for communicating with the REST API.
# Attributes: base_url, country_endpoint, leaders_endpoint, cookies_endpoint, and session (optional: utilizing a persistent requests.Session()).
# Methods:
# refresh_cookie(): Checks validity and refreshes the session cookie when expired.
# get_countries(): Queries the API and returns a clean list of supported country codes.
# get_leaders(country: str): Fetches and returns the raw JSON list of leaders for a targeted country.

