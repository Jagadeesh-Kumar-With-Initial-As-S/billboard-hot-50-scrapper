---

[Sparta Coding Club] BE Week 1 And Solution Of Homework Week 1
During the BE week one Python was explained.
Here are a few things you should know before diving into learning the Python syntax…
Python is a very intuitive language, and there is a lot it can do. However it is difficult for developers to remember all of the syntax of Python. Apart from learning it today, we encourage you to google and find what you need if you ever get stuck!
Some features of the Python language, such as tuples, sets, and classes will not be covered in this basic tutorial. It's okay if you don't know these features for now. However, we encourage you to explore these topics on your own time, as they can become powerful tools in your programming toolbox.

 web scraping (movie title)
[Code Snippet] IMDb top rated movies

<https://www.imdb.com/chart/top/?ref_=nv_mv_250>
Installing additional packages (beautifulsoup4)

bs4
Basic settings for crawling
[Code Snippet] Crawling default settings

import requests from bs4 import BeautifulSoup  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'} 
data = requests.get('<https://www.imdb.com/chart/top/?ref_=nv_mv_250>',headers=headers)  
soup = BeautifulSoup(data.text, 'html.parser')  
# Start coding

Learn how to use select / select_one in BeautifulSoup
 👉 Retrieve the movie title, year, and rating
 👉 When you want to get the text inside a tag → tag.text When you want to get an attribute in a tag → tag ['attribute']

import requests from bs4 import BeautifulSoup  
# Read the URL and get the HTML, 
headers = {     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' }  
# You will be scraping the data from this page 
url = '<https://www.imdb.com/chart/top/?ref_=nv_mv_250>'  
# Use the requests library to get the HTML code at the url above 
data = requests.get(url=url, headers=headers)  
# The BeautifulSoup library makes it easy to 
# parse HTML code 
soup = BeautifulSoup(data.text, 'html.parser')  
# Using select 
movies = soup.select('.lister > table > tbody > tr')  
# Looping through the movies for movie in movies:     
# First, let's get the title of the movie     
movie_title = movie.select_one('.titleColumn > a').text   
print(movie_title)
Learn the different ways you can use the select method in beautifulsoup

# How to use selector (copy selector) 
soup.select('tag name') 
soup.select('.class name') soup.select('#ID name')  
soup.select('upper tag name > sub tag name> sub tag name') 
soup.select('higher tag name.class name > subtag name.class name')  
# How to find by tag and attribute value 
soup.select('tag name[attribute="value"]')  
# If you only want to bring one 
soup.select_one('same as above')

It's not always accurate, but you can also refer to the Chrome Developer Tools.

Right-click on the desired part → Inspect
Right-click on the desired tag
Selector can be copied by first right-clicking an element, clicking Copy → Copy selector

Week 1 Homework
Try scraping the #1~50 songs of Billboard
📂 week3 > New > HTML File > music.html
[Code Snippet] Billboard The Hot 100

<https://www.billboard.com/charts/hot-100>
Just scrape the rank / song title / singer.
Q. If this happens, you've succeeded!
 👻 HINT:
The rankings and titles will not come out neatly. There is a space on the side, other letters appear, etc… Please study the Python built-in function strip() well!

---

Solution of Homework Week 1
billboard hot 50 scrapper using Python
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
Screenshots

Coding with Python

Output of the coding in Python
Github
The code is uploaded on https://github.com/Jagadeesh-Kumar-With-Initial-As-S/billboard-hot-50-scrapper .
Medium
The blog about [Sparta Coding Club] BE Week 1 And Solution Of Homework Week 1 is on https://medium.com/p/de90c55c4bc3/
Conclusion
The homework of BE Week one is successfully completed.
