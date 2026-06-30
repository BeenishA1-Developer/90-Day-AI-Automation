# day19.py — Combine 2 APIs together (real automation pattern)
import requests

def get_random_advice():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['slip']['advice']
        return None
    except Exception as e:
        print(f"Error fetching advice: {e}")
        return None

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{data['setup']} ... {data['punchline']}"
        return None
    except Exception as e:
        print(f"Error fetching joke: {e}")
        return None

def daily_digest():
    print("=== Your Daily Digest ===\n")
    
    advice = get_random_advice()
    if advice:
        print(f"💡 Advice of the day: {advice}\n")
    
    joke = get_random_joke()
    if joke:
        print(f"😂 Joke of the day: {joke}\n")

def main():
    daily_digest()

main()