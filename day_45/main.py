import requests
from bs4 import BeautifulSoup

# retrieve website data
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
top_movies_website = response.text
soup = BeautifulSoup(top_movies_website, 'html.parser')

# selects the movie titles
top_movies = soup.select('h3')
movies = [movie.get_text() for movie in top_movies]
reversed_movies = movies[::-1]

# create txt file
with open('top 10 movies of all time.txt', 'w', encoding='utf-8') as movie_list:
    for movie in reversed_movies:
        movie_list.write(f"{movie}\n")
