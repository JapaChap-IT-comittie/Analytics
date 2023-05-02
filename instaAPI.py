import requests
import json
url = "https://instagram28.p.rapidapi.com/media_likers"

short_code = input("URL >>>")
querystring = {"short_code":short_code}

headers = {
	"X-RapidAPI-Key": "3992152cf9mshc9d22576d21102ep1f3ec8jsn8496315103dc",
	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())