import requests
import config


class Kinopoisk_testing_api:
    def __init__(self, base_url_api: str, api_key=None):
        self.base_url = base_url_api
        self.api_key = api_key

    def connect_to_api_with_params(self, params=None):
        """
        Request without a mandatory endpoint, only parameters.
        """
        url = self.base_url
        headers = {
            'X-API-KEY': config.auth_token,
            'accept': 'application/json'
            }
        response = requests.get(url, headers=headers, params=params)
        return response

    def connect_to_api_with_endpoint(self, endpoint: str, params=None):
        """
        Request with a mandatory endpoint and parameters.
        """
        url = self.base_url + endpoint
        headers = {
            'X-API-KEY': config.auth_token,
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers, params=params)
        return response

    def search_movie_by_id(self, movie_id: int):
        """
        Request to get movie details by ID.
        """
        endpoint = f"/{movie_id}"
        params = {}
        return self.connect_to_api_with_endpoint(endpoint, params)

    def search_movie_with_query(self):
        """
        A request with a parameter to retrieve information, for example, a movie.
        """
        endpoint = "/search"
        params = {
            "page": config.page,
            "limit": config.limit,
            "query": config.search_query
            }
        return self.connect_to_api_with_endpoint(endpoint, params=params)

    def alternative_searching(self):
        """
        A request to retrieve movie information using alternative
        parameters, such as release year and movie rating.
        """
        params = {
            "page": config.page,
            "limit": config.limit,
            "releaseYears.start": config.years,
            "rating.kp": config.rating
            }
        # Logging the request parameters
        print(f"Request parameters: {params}")
        response = self.connect_to_api_with_params(params=params)
        # Logging the response for diagnostics
        print(f"API response: {response.text}")
        return response.json()

    def search_genre_and_interval(self):
        """
        Request for movie information by alternative parameters,
        such as release year and movie genre.
        """
        params = {
            "page": config.page,
            "limit": config.limit,
            "year": config.years,
            "genres.name": config.genre
            }
        # Logging the request parameters
        print(f"Request parameters: {params}")
        response = self.connect_to_api_with_params(params=params)
        # Logging the response for diagnostics
        print(f"API response: {response.text}")
        return response.json()

    def search_actor_with_query(self):
        """
        Request with parameters to retrieve information about an actor.
        """
        endpoint = "/search"
        params = {
            "page": config.page,
            "limit": config.limit,
            "query": config.actor_api
            }
        return self.connect_to_api_with_endpoint(endpoint, params=params)
