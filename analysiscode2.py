import requests as req  # to Make a request to a web page, and print the response text
from bs4 import BeautifulSoup  # Beautiful Soup is a Python library for pulling data out of HTML and XML files
import re
import json

jsondict={}

def dictionary_func(titlename,genrename,yearentry,rating):
    subjsondict = {}

    subjsondict["Title Name"] = titlename
    subjsondict["Genre"] = genrename
    subjsondict["Year"]= yearentry
    subjsondict["Rating"] = rating

    return subjsondict


webpage_html = req.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")

# print(webpage_html.status_code)# if 200 - page has been downloaded succesfully
soup = BeautifulSoup(webpage_html.text, 'lxml')  # Specifying the HTML parser we want to use.
for points in soup.find_all('div', {"class": "lister-item-content"}):

    point1 = points.find('span', {"class": "lister-item-index unbold text-primary"}).get_text().replace(".","")
    titlename = points.find('a', {'href': re.compile('/title/')}).get_text()
    genrename = points.find('span', {"class": "genre"}).get_text().strip()
    yearentry = points.find('span', {"class": "lister-item-year text-muted unbold"}).get_text()
    yearentry = yearentry.replace("(", "")
    yearentry = yearentry.replace(")", "")
    yearentry = yearentry.replace(" ", "")
    rating = points.find('div', {"class": "inline-block ratings-imdb-rating"})['data-value']

    jsondict[point1]=dictionary_func(titlename,genrename,yearentry,rating)

with open('jsondict.json', 'w') as outfile :
    json.dump(jsondict,outfile)

