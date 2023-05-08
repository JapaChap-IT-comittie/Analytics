import requests,json,csv

url = "https://instagram28.p.rapidapi.com/media_info_v2"

shortURL = input('>>> ShortURL')
querystring = {"short_code":shortURL}

headers = {
	"X-RapidAPI-Key": "3992152cf9mshc9d22576d21102ep1f3ec8jsn8496315103dc",
	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
}

# APIから情報取得、json化
res = requests.get(url, headers=headers, params=querystring)
data = res.json()

# JsonPath = "./data2.json"
# with open(JsonPath, 'w', encoding='utf8') as f:
#         "{}".format(json.dump(response.json(), f, ensure_ascii=False,indent=2))
# with open(JsonPath,'r',encoding='utf8') as f:
#     data = json.load(f)

# 必要なデータの抽出 videoファイルのpostはjsonの形式が異なる
try:
    like = data["items"][0]["like_count"]
    short = data["items"][0]["code"]
    info = data["items"][0]["carousel_media"][0]["accessibility_caption"]
    URL = f"https://www.instagram.com/p/{short}"
    print(f"{like}\n{short}\n{info}")
    # CSV ファイルを開いてヘッダーを書き込む
    header = ["URL","LikeCount","info"]
    csvPath = "./output2.csv"
    with open(csvPath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([URL,like,info])
except:
    print("Now only available to use posts, not including video")






