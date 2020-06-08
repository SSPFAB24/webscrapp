import requests as req  # to Make a request to a web page, and print the response text
from bs4 import BeautifulSoup  # Beautiful Soup is a Python library for pulling data out of HTML and XML files
import re
import json


webpage_html = req.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")
movielist=[]
# print(webpage_html.status_code)# if 200 - page has been downloaded succesfully
soup = BeautifulSoup(webpage_html.text, 'lxml')  # Specifying the HTML parser we want to use.
for points in soup.find_all('div', {"class": "lister-item-content"}):
    movie=[]
    point1 = points.find('span', {"class": "lister-item-index unbold text-primary"}).get_text().replace(".","")
    print(point1, end=" ")
    movie.append(point1)

    titlename = points.find('a', {'href': re.compile('/title/')}).get_text()
    print(titlename, end=" ")
    movie.append(titlename)

    genrename = points.find('span', {"class": "genre"}).get_text().strip()
    print(genrename, end=" ")
    movie.append(genrename)

    yearentry = points.find('span', {"class": "lister-item-year text-muted unbold"}).get_text()
    yearentry = yearentry.replace("(", "")
    yearentry = yearentry.replace(")", "")
    yearentry = yearentry.replace(" ", "")
    print(yearentry.strip(), end=" ")
    yearentry=yearentry.strip()
    movie.append(yearentry)

    rating = points.find('div', {"class": "inline-block ratings-imdb-rating"})['data-value']
    print(rating, end=" ")
    movie.append(rating)

    # for loop1 in points.find_all('div',{"class":"inline-block ratings-imdb-rating"}):
    # rating= str(points.:q!
    # find('strong').get_text()).strip()
    # print(rating)
    movielist.append(movie)

    print()
jsondict={}
for i in movielist:
    subjsondict={}

    subjsondict["Movie name"] = i[1]
    subjsondict["Year"]= i[3]
    subjsondict["Rating"] = i[4]
    jsondict[i[0]]=(subjsondict)

jsondict_dump = json.dumps(jsondict)#to convert to json format
print(jsondict_dump)


