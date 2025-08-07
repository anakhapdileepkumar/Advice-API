import requests

url = "https://api.adviceslip.com/advice"
response = requests.get(url)
data = response.json()

advice = data['slip']['advice']
print("🧠 Random Advice:", advice)
