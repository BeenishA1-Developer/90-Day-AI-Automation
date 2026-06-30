# day18.py — Secure API Call using OpenRouter Free Tier
import os
from openai import OpenAI
from dotenv import load_dotenv

# .env file se keys load karein
load_dotenv()

# OpenRouter client initialize karein
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            # Free aur stable model
            model="google/gemini-2.5-flash", 
            messages=[
                {"role": "user", "content": question}
            ],
            # Free account limit ke mutabiq tokens restrict kiye
            max_tokens=50 
        )
        print("\n🤖 AI Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Day 18: OpenAI API ===")
    ask_ai("Explain APIs in one simple sentence for a beginner.")

main()