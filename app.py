# app.js
# import flask modules

from flask import *

# construct the code app objects
app = Flask(__name__)

# configure settings and Initialize plugins
app.config.from_object('settings.Config')

with app.app_context():
	from routes import index

	# register the index route 
	app.register_blueprint(index.index_bp)

