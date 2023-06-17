from app import app

if __name__ == '__main__':
	# DEBUG is set to TRUE. Change to FALSE for production
	app.run(host='0.0.0.0', port=3000)