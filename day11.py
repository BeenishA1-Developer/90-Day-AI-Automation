# day11.py — PIP & Libraries
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        print(f"Weather: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

user_city = input("Enter city name for weather update: ")
get_weather(user_city)