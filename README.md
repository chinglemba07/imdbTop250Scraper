## IMDb Top Movies Scraper
This Python script is designed to scrape the top-rated movies from IMDb and store the data in a JSON file.

## Prerequisites
Make sure you have the following dependencies installed:

* requests: Used for making HTTP requests to retrieve the IMDb webpage.
* json: Used for working with JSON data.
* pandas: Used for data manipulation and analysis (not explicitly used in this script).
* bs4 (Beautiful Soup): Used for parsing HTML and extracting data from it.

You can install these dependencies using pip:

		pip install -r requirements.txt

The requirements.txt file contains a list of dependencies and their versions.

## Usage
Import the necessary modules:

	import requests
	import json
	import pandas as pd
	from bs4 import BeautifulSoup
Set the URL of the IMDb top movies page:

	url = "https://www.imdb.com/chart/top/"
Send an HTTP GET request to the URL and retrieve the webpage content:

	response = requests.get(url)
	response = response.content
Create a BeautifulSoup object to parse the HTML content:
	
	soup = BeautifulSoup(response, 'html.parser')
Find all the movie elements in the HTML using the appropriate CSS selectors:

	ol = soup.find_all('td', class_='titleColumn')
	rt = soup.find_all('strong')
Iterate over the movie elements and extract the desired information:

	movie_list = []


	for i in range(len(ol)):
    rank = i + 1
    tr = ol[i].find('a')
    title = tr.text
    yr = ol[i].find('span', class_='secondaryInfo')
    year = int(yr.text[1:5])
    actors = tr.attrs["title"]
    split_actors = actors.split("(dir.),")
    director = split_actors[0].strip()
    cast = split_actors[1].strip()
    rating = float(rt[i].text)
    
    movie_list.append({
        "rank": rank,
        "title": title,
        "year": year,
        "director": director,
        "cast": cast,
        "rating": rating
    })
Write the extracted movie data to a JSON file named data.json:

	with open('data.json', 'w') as file:
    json.dump(movie_list, file)
Note: The script uses the json.dump() function to write the data in a structured format. 
You can modify the script to perform additional data processing or analysis based on your requirements.
