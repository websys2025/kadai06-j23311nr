import requests

App_URL = "https://dataset.city.shizuoka.jp/dataset/dcefcb5c-6b09-42a6-92d8-3e360c87a5ef/resource/941aaaa8-ac95-4348-a37d-5b01d3a613f5/download/kyuugosyo.json"

response = requests.get(App_URL)
data = response.json()

print(data)