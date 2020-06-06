import requests as req  # to Make a request to a web page, and print the response text
from bs4 import BeautifulSoup  # Beautiful Soup is a Python library for pulling data out of HTML and XML files
import re

webpage_html = req.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")

# print(webpage_html.status_code)# if 200 - page has been downloaded succesfully
soup = BeautifulSoup(webpage_html.text, 'lxml')  # Specifying the HTML parser we want to use.
for points in soup.find_all('div', {"class": "lister-item-content"}):
    point1 = str(points.find('span', {"class": "lister-item-index unbold text-primary"}).get_text())
    print(point1, end=" ")

    titlename = str(points.find('a', {'href': re.compile('/title/')}).get_text())
    print(titlename, end=" ")

    genrename = str(points.find('span', {"class": "genre"}).get_text()).strip()
    print(genrename, end=" ")

    yearentry = str(points.find('span', {"class": "lister-item-year text-muted unbold"}).get_text())
    yearentry = yearentry.replace("(", "")
    yearentry = yearentry.replace(")", "")
    yearentry = yearentry.replace(" ", "")
    print(yearentry.strip(), end=" ")

    rating = points.find('div', {"class": "inline-block ratings-imdb-rating"})['data-value']
    print(rating, end=" ")

    # for loop1 in points.find_all('div',{"class":"inline-block ratings-imdb-rating"}):

    # rating= str(points.find('strong').get_text()).strip()
    # print(rating)

    print()