"""
	File name:  app.py
	In this app.py file, you have to define app
	and import the routes and register the blueprint
	import Flask module
"""
from flask import Flask

# construct the code app objects
app = Flask(__name__)

# configure settings and Initialize plugins
app.config.from_object('settings.Config')

with app.app_context():
	from routes import index
	# register the index route 
	app.register_blueprint(index.index_bp)

