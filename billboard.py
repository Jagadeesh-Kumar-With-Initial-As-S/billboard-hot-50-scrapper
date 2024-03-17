import requests
from bs4 import BeautifulSoup

# You will be scraping the data from this page
url = "https://www.billboard.com/charts/hot-100"
# Read the URL and get the HTML,
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

data = requests.get(url=url, headers=headers)

# The BeautifulSoup library makes it easy to parse HTML code
soup = BeautifulSoup(data.text, "html.parser")

song_cont = soup.find("div", class_="chart-results-list")
songs = song_cont.find_all("div", class_="o-chart-results-list-row-container")

# Looping through the songe
for i in range(50):
    # First, let's get the title of the movie
    song = songs[i]
    song_name = song.find("h3", class_="c-title").text.strip()

    h1 = song.find("li", class_="lrv-u-width-100p")
    h2 = h1.find("li", class_="o-chart-results-list__item")
    song_artist = h2.find("span", class_="c-label").text.strip()

    print(f"{i+1} / {song_name} / {song_artist}")