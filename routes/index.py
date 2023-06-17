# routes/index.py 
# route to templates page
from flask import (Flask, url_for, 
	render_template, Blueprint, 
	request, current_app)
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
	try:
		# Get the search parameters from query parameters
		# topic = request.args.get('topic')
		# rating = request.args.get('rating')

		return render_template('index.html')
	except TemplateNotFound:
		abort(404)


# route to the search page
@index_bp.route('/repos/', methods=['POST'])
def search():
    # Get the selected values from the form
    topic = request.form.get('topic')
    rating = request.form.get('rating')
    language = request.form.get('language')
    repositories = Filter.search_repositories_by_topic(language, topic, rating, current_app.config['TOKEN'])
    filtered_repos = []
    if repositories is not None:
    	for repo in repositories:
            #if repo['stargazers_count'] >= int(rating):
            filtered_repos.append(repo)

    # Redirect to the result page with search parameters as query parameters
    return  render_template('result.html', topic=topic, rating=rating, repositories = filtered_repos)