# http://vaaaaaanquish.hatenablog.com/entry/2017/06/25/202924#--%E3%82%A2%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%80--
# urllibではなくrequestsを使うように改変
import requests
from bs4 import BeautifulSoup

# ヘッダーを設定する
headers = {"Accept-Language": "en-US,en;q=0.5","User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Referer": "http://thewebsite.com","Connection": "keep-alive"}

# まずは一つのurlからスクレイピング
url = 'https://safebooru.org/index.php?page=post&s=view&id=2429568'
resp = requests.get(url, timeout=1, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")
img_tag = soup.find("img", id="image")

name = img_tag.find()
# 仮でファイルに書き込み。多分だけど、textが文字列取得だと思います。。
with open('str.txt', 'w') as f:
  f.write(resp.text)



