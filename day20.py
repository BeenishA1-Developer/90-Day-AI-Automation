# day20.py — OpenAI + Public API combined (Fixed Integration)
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# OpenRouter client setup with correct base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_advice():
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['slip']['advice']
    except Exception as e:
        print(f"Advice API Error: {e}")
    return "Work hard every day."

def ai_expand_advice(advice):
    try:
        response = client.chat.completions.create(
            model="google/gemini-2.5-flash",  # Using the reliable free tier model
            messages=[
                {"role": "user", "content": f"Expand this advice in 2 sentences for a young developer: {advice}"}
            ],
            max_tokens=60
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {e}"

def main():
    print("=== AI-Powered Daily Advice ===\n")
    advice = get_advice()
    print(f"Raw Advice: {advice}\n")
    expanded = ai_expand_advice(advice)
    print(f"AI Expanded: {expanded}")

main()