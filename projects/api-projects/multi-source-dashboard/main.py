# os is a built-in python tool for interacting with your OS
# dotenv is the package we installed.
# os.getenv() is a special method. If it finds the variable name you asked for, it returns the value as a String. If it doesn't find it, it returns a special Python type called None.
# if api_key: is a shorthand trick in Python. Python evaluates an empty variable or None as False, and a text string containing data as True.
# Install first: pip install python-dotenv first when creating this program initially. I already did that.
# -----------------------------------------
# IMPORTS
# -----------------------------------------
import os
import json
import requests
from dotenv import load_dotenv

# -----------------------------------------
# ENVIRONMENT SETUP
# -----------------------------------------
# Load the secret file into memory (this is in the same directory as main.py)
load_dotenv()
# Grab the secret key and store it in a variable
weather_key = os.getenv("WEATHER_API_KEY")
news_key = os.getenv("NEWS_API_KEY")


# -----------------------------------------
# WEATHER API
# -----------------------------------------

# Set up search parameters with UPPERCASE VARIABLES to signal the value will be a Constant and should never change
CITY = "Olathe"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={weather_key}&units=imperial"


# Send request to the internet and save the response
# weather_response as a physical toolbox. Inside this toolbox there are several compartments (attributes and methods).
# print the status code to see if the server accepted the req
# When we type weather_response.status_code, the dot (.) means "Open up the weather_response toolbox and look inside the pre-built compartment named status_code."
# Because weather_response holds the entire toolbox, you can look inside different compartments right now without changing any other code:weather_response.status_code holds the number 200.weather_response.url holds the exact web address that was targeted.weather_response.text holds the raw, giant wall of weather text data sent by the server.You only created one variable: weather_response. The .status_code part is a built-in feature of that variable because it is a Response Object!
weather_response = requests.get(URL)
# print(f"Server response status code: {weather_response.status_code}")

# the main compartment of the toolbox is .json()
# convert to a python object
weather_data_object = weather_response.json()
# pretty print that cuz nobody can understand a block of text
# print(json.dumps(weather_data_object, indent=4))

# Extract current temperature
# Look inside the main directory in the data and grab the temp key
# the square brackets are being used to look up keys in a dictionary and will grab the key:value pair
current_temp = weather_data_object["main"]["temp"]

# extract weather description
# used index of 0 bcuz this data is in a list and may hold multiple things.  if you only want one, u need to specify which (the first in this case)
weather_desc = weather_data_object["weather"][0]["description"]

# test extractions
# print(f"\n🌤️ extracted data preview:")
# print(f" Temp: {current_temp}°F")
# print(f" Condition: {weather_desc}")

# -----------------------------------------
# NEWS API
# -----------------------------------------


# Setup Mediastack constants
NEWS_DATE_RANGE = "2026-05-01,2026-05-31"
COUNTRY = "us"
LANGUAGE = "en"
CATEGORY = "technology"
LIMIT = 5

# Construct Mediastack URL using news_key variable and mediastacks requirements

NEWS_URL = (
    f"https://api.mediastack.com/v1/news"
    f"?access_key={news_key}"
    f"&date={NEWS_DATE_RANGE}"
    f"&countries={COUNTRY}"
    f"&languages={LANGUAGE}"
    f"&categories={CATEGORY}"
    f"&limit={LIMIT}"
)

# request to the news server
news_response = requests.get(NEWS_URL)

# convert to json obj then see data and store data in news_data
news_data = news_response.json()
# print(news_data.keys())

# Go into the response that you get back and find me the keyword "data" then store it in articles
articles = news_data["data"]

# For each single article inside the collection called articles, take one out temporarily and call it article then run the code below it
for article in articles:
    # what do we want to do with the article? we want to store each value into a variable to use later
    title = article["title"]
    source = article["source"]
    description = article["description"]

    print(f"{title}")
    print(f"Source: {source}")
    print(f"{description}")
    print("-" * 50)
