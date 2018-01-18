import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}

u = 'http://catindog.hatenablog.com/archive/2017/'
links = []

for page in range(11):
  url = u + str(page + 1)
  #print(url)
  resp = requests.get(url, timeout=1, headers=headers)
  soup = BeautifulSoup(resp.text, 'html.parser')
  a_tag = soup.find_all('a', class_='entry-title-link')
  #print(a_tag)
  #if len(a_tag) > 1:
  for a in a_tag:
    print(a['href'])
  #else:
   # print(a_tag['href'])

#links.append(link)

#with open('link.txt', 'w') as l:
 # for li in links:
  #  l.write(li)

