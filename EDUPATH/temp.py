import requests

API_KEY = 'AIzaSyB6woFSAW5gEz0vGAihK_yKrJ_FjpwvUnA'
prompt = "Explain how AI works"

url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}'
headers = {
    'Content-Type': 'application/json'
}
data = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
response_text = response.json()['candidates'][0]['content']['parts'][0]['text']


print(response_text)