from app import app

if __name__ == '__main__':
	# DEBUG is set to TRUE. Change to FALSE for production
	app.run(host='localhost', port=3000)