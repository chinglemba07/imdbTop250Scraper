import requests
import json

import pandas as pd

from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"

response=requests.get(url)

response=response.content

soup=BeautifulSoup(response,'html.parser')

ol=soup.find_all('td',class_='titleColumn')

rt=soup.find_all('strong')

movie_list=[]

for i in range(len(ol)):
  rank=i+1
  # print("Rank :",rank)

  tr=ol[i].find('a')
  title=tr.text
  # print("Title:",title)

  yr=ol[i].find('span',class_='secondaryInfo')
  year=int(yr.text[1:5])
  # print("Year:",year)

  actors=tr.attrs["title"]
  split_actors = actors.split("(dir.),")
  # Get the characters before "(dir.)" (at index 0)
  director = split_actors[0].strip()
  cast = split_actors[1].strip()

  # print("Actors:",actors)

  rating=float(rt[i].text)
  # print("Rate:",rating)

  movie_list.append({"rank":rank,"title":title,"year":year,"director":director,"cast":cast,"rating":rating})

# print(movie_list)

# Write data to data.json
with open('data.json', 'w') as file:
    json.dump(movie_list, file)
