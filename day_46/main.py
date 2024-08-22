import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Secrets
SPOTIFY_CLIENT_ID = getenv('CLIENT_ID')
SPOTIFY_CLIENT_SECRET = getenv('CLIENT_SECRET')
SPOTIFY_USER_NAME = getenv('USERNAME')

# extracting data into soup
songs_date = input("Which year do you want to travel to in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{songs_date}/"
response = requests.get(url)
top_100_songs = response.text
soup = BeautifulSoup(top_100_songs, 'html.parser')

# retrieving song name
song_titles = soup.select('li ul li h3')
songs = [song.get_text().replace('\n', '').replace('\t', '') for song in song_titles]


# Spotify
playlist_uri = f"http://example.com"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=playlist_uri,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USER_NAME
    )
)

user_id = sp.current_user()["id"]


# search for the songs
song_uris = []
year = songs_date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

print(song_uris)

# creates a playlist and adds music to the playlist
playlist = sp.user_playlist_create(user=user_id, name=f"Throwback Songs of {songs_date}", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
