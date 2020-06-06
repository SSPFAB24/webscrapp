import requests as req  # to Make a request to a web page, and print the response text

from bs4 import BeautifulSoup  # Beautiful Soup is a Python library for pulling data out of HTML and XML files
import re

webpage_html = req.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")

#print(type(webpage_html.content))
# print(webpage_html.status_code)# if 200 - page has been downloaded succesfully

soup = BeautifulSoup(webpage_html.text, 'lxml')  # Specifying the HTML parser we want to use.

# print(soup.encode("utf-8").find('div', attrs={'class':'lister-item-content'}).text)
for points in soup.find_all('div', {"class": "lister-item-content"}):
    for points_1 in points.find_all('span', {"class": "lister-item-index unbold text-primary"}):
        point1 = str(points_1.text)
        print(point1, end=" ")

    for link in points.find_all('a', {'href': re.compile('/title/')}):
        print(link.get_text(), end=" ")
        break
        # print("a", end =" ")
    for points_3 in points.find_all('span', {"class": "runtime"}):
        point3 = str(points_3.text)
        print(point3, end=" ")

    for points_2 in points.find_all('span', {"class": "lister-item-year text-muted unbold"}):
        point2 = str(points_2.text)
        print(point2, end=" ")
    print()