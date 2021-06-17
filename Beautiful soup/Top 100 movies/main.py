from bs4 import BeautifulSoup
import requests

resource = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = resource.text
soup = BeautifulSoup(empire_web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
print(all_movies)
movie_titles =[]
for movie in all_movies:
    movie_titles.append(movie.gettext())

with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
