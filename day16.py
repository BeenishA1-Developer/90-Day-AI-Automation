# day16.py — POST Request + Query Parameters
import requests

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    data = {
        "title": "AI Automation Journey",
        "body": "Learning APIs on Day 16",
        "userId": 1
    }
    
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 201:
            print("Post created successfully!")
            print(response.json())
        else:
            print(f"Failed: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def search_with_params():
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        posts = response.json()
        print(f"\nFound {len(posts)} posts for userId 1")
        for p in posts[:3]:
            print(f"- {p['title']}")

def main():
    print("=== POST Request ===")
    create_post()
    
    print("\n=== GET with Parameters ===")
    search_with_params()

main()