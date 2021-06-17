from bs4 import BeautifulSoup
import requests
import datetime
import calendar


date_input = input("Type the date in this format YYYY-MM-DD: ")


URL = "https://www.billboard.com/charts/hot-100/" + date_input
song_list = requests.get(URL)

soup = BeautifulSoup(song_list.text, "html.parser")
songs_info = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

filename = "top100_" + date_input + ".txt"
with open(filename, mode="a") as f:
    for i in songs_info:
        temp = i.text + "\n"
        f.write(temp)
