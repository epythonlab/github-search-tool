"""
Filter Model

This module provides functionality for searching repositories on GitHub based on various filters.

Attributes:
    None

Methods:
    search_repositories_by_topic(language, topic, min_rating, token):
        Searches repositories on GitHub based on the specified filters.
    get_next_page_url(headers): Retrieves the URL of the next page in the paginated response.

"""
import json
import requests


class Filter:
    """
    Filter Model

    This class provides functionality for searching repositories on GitHub based on various filters.

    Attributes:
        None

    Methods:
        search_repositories_by_topic(language, topic, min_rating, token):
            Searches repositories on GitHub based on the specified filters.
        get_next_page_url(headers): Retrieves the URL of the next page in the paginated response.

    """

    def __init__(self):
        pass

    @staticmethod
    def search_repositories(language, topic, min_rating, token):
        """
        Search repositories on GitHub based on the specified filters.

        Args:
            language (str): The programming language to filter by.
            topic (str): The topic or tag to filter by.
            min_rating (int): The minimum rating (stars) a repository should have.
            token (str): The GitHub API token for authentication.

        Returns:
            list: A list of repository objects matching the specified filters.

        """
        headers = {
            'Authorization': f'Token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }

        # url = f'https://api.github.com/search/repositories?q=topic:{topic}+stars:>{min_rating}'
        # search query contains
        # lanuague, topic or tag and name contains the selected topic
        # rating
        query = f'language:{language}+in:topic+{topic}+stars:>{min_rating}+in:name+{topic}'
        sort = 'stars'  # Sort by stars (rating)
        url = f'https://api.github.com/search/repositories?q={query}&sort={sort}'

    # store the results in the list
        repositories = []

        while url:
            response = requests.get(url, headers=headers, timeout=10)
            response_json = json.loads(response.text)

            if response.status_code == 200:
                repositories.extend(response_json['items'])
                url = Filter.get_next_page_url(response.headers)
            else:
                print(
                    f"Request failed with status code {response.status_code}")
                break

        return repositories


    @staticmethod
    def get_next_page_url(headers):
        """
        Retrieve the URL of the next page in the paginated response.

        Args:
            headers (dict): The header information of the response.

        Returns:
            str: The URL of the next page, or None if there is no next page.

        """
        link_header = headers.get('Link')
        if link_header:
            links = link_header.split(', ')
            for link in links:
                if 'rel="next"' in link:
                    return link[link.index('<')+1:link.index('>')]
        return None
