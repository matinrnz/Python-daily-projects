import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_names = [movie.getText() for movie in movies]
movie_names.reverse()
with open("movies.txt", mode="w", encoding='utf-8') as file:
    for movie_name in movie_names:
        file.write(f"{movie_name}\n")
