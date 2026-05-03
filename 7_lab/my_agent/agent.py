import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Спробуємо максимально просту модель gemini-pro (1.0)
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

data = {
    "contents": [{"parts": [{"text": "Привіт! Напиши 'Агент KN-210 у строю'."}]}]
}

print("Спроба №1 (gemini-pro)...")
response = requests.post(url, json=data)

if response.status_code != 200:
    print("Не спрацювало. Остання спроба (модель text-bison)...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/text-bison-001:generateContent?key={api_key}"
    response = requests.post(url, json=data)

if response.status_code == 200:
    print("\n" + "="*20)
    print("ВІДПОВІДЬ:")
    print(response.json()['candidates'][0]['content']['parts'][0]['text'])
    print("="*20)
else:
    print(f"\nНа жаль, Google Studio блокує доступ: {response.text}")
    print("Порада: Спробуй створити НОВИЙ API-ключ в Google AI Studio.")