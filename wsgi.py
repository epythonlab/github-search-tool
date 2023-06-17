"""File name: wsgi.py
	run this file only
	Run: python3 wsgi.py on terminal
	- change the host in production
	- change the debug to False in production
	- change port as needed
"""
from app import app
if __name__ == '__main__':
	# DEBUG is set to TRUE. Change to FALSE for production
	app.run(host='0.0.0.0', port=3000)
