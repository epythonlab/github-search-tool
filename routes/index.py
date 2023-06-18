"""
routes/index.py

This module defines the routes for the Flask application.
It contains routes for the index page and the search page.

Routes:
- index: Renders the index page.
- search: Handles the search form submission and renders the result page.

"""

from flask import (render_template, Blueprint, request, current_app)
from models.filter import Filter


# create and configure the blueprint
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
# define the route path


@index_bp.route('/', methods=['GET'])
def index():
    """
    Renders the index page.

    Returns:
        The rendered index page template.
    """
    return render_template('index.html')


# route to the search page
@index_bp.route('/repos/', methods=['POST'])
def search():
    """
    Handles the search form submission and renders the result page.

    Returns:
        The rendered result page template with the search parameters and filtered repositories.
    """
    topic = request.form.get('topic').replace(' ', '-')
    rating = request.form.get('rating')
    language = request.form.get('language')
    repositories = Filter.search_repositories(language, topic, rating, current_app.config['TOKEN'])
    filtered_repos = []
    if repositories is not None:
        for repo in repositories:
            # if repo['stargazers_count'] >= int(rating):
            filtered_repos.append(repo)

    # Redirect to the result page with search parameters as query parameters
    return render_template('result.html', topic=topic, rating=rating, repositories=filtered_repos)
