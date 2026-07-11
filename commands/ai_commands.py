import requests
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL
from voice import speak


def ask_ai(prompt):
    prompt = prompt.strip()

    if not prompt:
        speak("What should I ask AI?")
        return

    if not OPENROUTER_API_KEY:
        speak("OpenRouter API key is missing. Please add it in the dot env file.")
        return

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        data = {
            "model": OPENROUTER_MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful laptop assistant AI."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()

        answer = result["choices"][0]["message"]["content"].strip()

        print("\nAI Response:\n")
        print(answer)
        speak("Here is the answer")

    except Exception as e:
        speak("AI request failed")
        print("AI error:", e)