# day17.py — PUT (update) + DELETE + Nested JSON parsing
import requests

def update_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    data = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated content - Day 17",
        "userId": 1
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            print("Post updated!")
            print(response.json())
        else:
            print(f"Update failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

def delete_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            print(f"Post {post_id} deleted!")
        else:
            print(f"Delete failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

def nested_json_practice():
    # Real APIs often return nested JSON like this
    data = {
        "name": {"common": "Pakistan", "official": "Islamic Republic of Pakistan"},
        "capital": ["Islamabad"],
        "population": 240000000
    }
    print(f"Country: {data['name']['common']}")
    print(f"Official Name: {data['name']['official']}")
    print(f"Capital: {data['capital'][0]}")
    print(f"Population: {data['population']:,}")

def main():
    print("=== PUT Request ===")
    update_post(1)

    print("\n=== DELETE Request ===")
    delete_post(1)

    print("\n=== Nested JSON Practice ===")
    nested_json_practice()

main()