# Filter Model 
# models/filter.py
import requests
import json
class Filter(object):

	def __init__(self):
		pass

	def search_repositories_by_topic(language, topic, min_rating, token):
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
	        response = requests.get(url, headers=headers)
	        response_json = json.loads(response.text)

	        if response.status_code == 200:
	            repositories.extend(response_json['items'])
	            url = get_next_page_url(response.headers)
	        else:
	            print(f"Request failed with status code {response.status_code}")
	            break

	    return repositories

"""
	method returns the links of pagination
	Args: header information including token
	Returns: url of each page
"""
def get_next_page_url(headers):
    link_header = headers.get('Link')
    if link_header:
        links = link_header.split(', ')
        for link in links:
            if 'rel="next"' in link:
                return link[link.index('<')+1:link.index('>')]
    return None

