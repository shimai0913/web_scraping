import lxml
import requests
import urllib.request
import os
import sys
from bs4 import BeautifulSoup

query_word = sys.argv[1] # コマンドラインで検索ワードを入れると、argv[1]に同値が入る。

URL = "https://www.google.com/search?biw=619&bih=760&tbm=isch&sxsrf=ACYBGNQtEj6poI66fJ-rDP3mNrpBDCNE3A%3A1580042225139&sa=1&ei=8YctXtyVCIu2mAX2nL2QAw&q={0}&oq=&gs_l=img.3..35i39j0l3j0i131j0i3j0l4.17915.17915..18593...0.0..0.76.147.2......0....2j1..gws-wiz-img.......0i4i37j0i4i3i37.M3k1TRe0KY8&ved=0ahUKEwic0rz8o6HnAhULG6YKHXZODzIQ4dUDCAc&uact=5".format(query_word)
headers = {"User-Agent": "hoge"}
resp = requests.get(URL, timeout=1, headers=headers)

soup = BeautifulSoup(resp.text, "lxml") # text形式で取れる

imgs = soup.find_all("img")

# 保存用ディレクトリ作成
dir_name = "./{0}".format(query_word)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    os.chdir("./{0}".format(dir_name))


for i in range(len(imgs)):
    # 「http」をURLに含んでいるもの
    if "http" in str(imgs[i]):
        # URL作成
        url_img = imgs[i]["src"]

        # リクエストを投げる
        res = requests.get(url_img)
        # レスポンスから画像部分だけ抽出
        image = res.content
        # 保存するときのファイル名
        filename = "{0}_{1}.jpg".format(query_word, str(i))

        # 任意の名前のファイル(file_name)をwb形式で開いています。ファイルがないときは作ってくれます。
        # 今回は、毎回とりあえず中身のないファイルを作り、それに画像データを書き込むということをしています。
        with open(filename, "wb") as aaa:
            aaa.write(image)




