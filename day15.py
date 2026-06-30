# day15.py — Fetch real data from a public API
import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()  # JSON string → Python dict
            print(f"Setup: {data['setup']}")
            print(f"Punchline: {data['punchline']}")
        else:
            print(f"Error: Status code {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

def main():
    print("=== Random Joke API ===")
    get_joke()

main()