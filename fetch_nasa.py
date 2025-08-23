import requests

API_KEY = "qHPlbha1R4YpK2DEipusif94FtU9ycpmUFrPmlFC"
API_URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

resp = requests.get(API_URL).json()
img_url = resp.get("hdurl") or resp.get("url")

img_data = requests.get(img_url).content
with open("nasa_bg.jpg", "wb") as f:
    f.write(img_data)
print("NASA foto kaydedildi:", img_url)
