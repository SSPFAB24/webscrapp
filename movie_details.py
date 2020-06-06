import requests as req
from bs4 import BeautifulSoup

movies_list = []

webpage_html = req.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")

soup = BeautifulSoup(webpage_html.content, "html.parser")

all_divs = soup.findAll("div", {"class": "lister-item-content"})
for div in all_divs:
    movie = []
    header3 = div.find("h3")
    movie_name = header3.find("a").text
    year = header3.find("span", {"class": "lister-item-year"}).text[1:][:-1]
    genre = div.find("p").find("span", {"class": "genre"}).text.strip()
    rating = div.find("strong").text
    movie.append(movie_name)
    movie.append(year)
    movie.append(genre)
    movie.append(rating)
    movies_list.append(movie)


print("Movie Name\t\t\tYear\tGenre\tRating")
for movie in movies_list:
    print("{}\t|\t{}\t|\t{}\t|\t{}".format(movie[0],movie[1],movie[2],movie[3]))
