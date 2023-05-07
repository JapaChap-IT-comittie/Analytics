import requests
import json
import csv

url = "https://instagram28.p.rapidapi.com/media_likers"

short_code = input("URL >>>")
querystring = {"short_code":short_code, "batch_size":"50"}

headers = {
	"X-RapidAPI-Key": "8521d63cc1mshdcd8e0a57ba8a10p129393jsn7e4b5761c530",
	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

# JSONデータをファイルに書き込む
with open("data.json", "w") as f:
    json.dump(data, f)

# # テスト用
# with open("data.json", "r") as f:
#     data = json.load(f)

# CSV ファイルに書き出すヘッダーを定義
header = ['count', 'full_name']

# CSV ファイルを開いてヘッダーを書き込む
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    # "count" と "full_name" のみを抽出して CSV ファイルに書き込む
    count = data['data']['shortcode_media']['edge_liked_by']['count']
    for node in data['data']['shortcode_media']['edge_liked_by']['edges']:
        full_name = node['node']['full_name']
        writer.writerow([count, full_name])
