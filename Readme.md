# Title: Github Repo Search Tool

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

The Github Repo Search Tool provides enhanced search functionality, allowing users to find repositories based on topics, ratings, and programming languages.

## Features

1. Search by Topic: The Github Repo Search Tool allows users to search for repositories based on specific topics. Users can enter a topic of interest, and the tool will retrieve repositories related to that topic.

2. Search by Top Rated: Users can search for repositories based on their rating or popularity. By specifying a minimum rating threshold, the tool fetches repositories that meet or exceed the specified rating.

3. Search by Language: The tool enables users to search for repositories written in specific programming languages. Users can select a programming language from the available options, and the tool will fetch repositories written in the chosen language.

4. Sorting by Top Rated: The search results can be sorted by the rating or popularity of the repositories. This feature allows users to view the repositories in descending order of their ratings, helping them identify the most highly rated repositories.

## Installation and Configuration

To install and use this project, please follow the steps below:

1. Install Python 3.x on your computer.
2. Clone the project by running the following command in your terminal:
  `git clone https://github.com/epythonlab/github-search-tool.git`

3. Navigate to the project's directory structure by running:
  `cd github-search-tool`

4. Set up and configure the virtual environment in the project directory:
  - Open your terminal and run the command:
  `python3 -m venv .venv`

  - Activate the virtual environment by running:
  `source .venv/bin/activate`

5. Install the required dependencies by running the command:

  `pip install -r requirements.txt`

7. Obtain your own token from GitHub and replace it in the `settings.py` file. Look for the line:
  `TOKEN = 'your token'`

Replace 'your token' with your actual token.

Once you have completed these steps, you should have the project installed and configured on your local machine. You can proceed to run the application and explore its features.

To run the server, execute the following command in your terminal:
  `python3 wsgi.py`

This will start the server, and you will be able to access the application by visiting the appropriate URL in your web browser.

## Usage

After installing and setting up the project, run the server using the command `python3 wsgi.py`.

Open your web browser and navigate to the URL where the server is running (usually `http://localhost:5000`).

On the home page, you will see a search form where you can specify your search criteria.
![Step 1](static/images/1.png)

Write a topic on the search bar and choose the programming language and rating from the drop-down menu as shown in the above picture to search for repositories related to that criteria.

Click on the "Search" button to initiate the search. It will show you the waiting message as shown below:
![Step 1](static/images/2.png)

The search results will be displayed on the next page, showing the repositories that match your criteria.

Each repository will be listed with its name, URL, star rating, fork count, and other relevant information.
![Step 1](static/images/3.png)

You can click on a repository to view more details and explore its contents.


To perform a new search, simply go back to the home page and enter new search criteria.

Enjoy exploring and discovering interesting GitHub repositories based on your search preferences!


## Contributing

If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Contact
You can reach out to us on the following platforms:
- Telegram: <i class="fab fa-telegram"></i>https://epythonlab.t.me/
- Facebook: <i class="fab fa-facebook"></i>https://facebook.com/epythonlab1/
- YouTube: <i class="fab fa-youtube"></i>https://youtube.com/@epythonlab/
- LinkedIn: <i class="fab fa-linkedin"></i>https://linkedin.com/company/epythonlab/
