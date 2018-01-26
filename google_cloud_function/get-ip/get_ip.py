import requests
import sys
import bs4  

r = requests.get('http://www.ugtop.com/spill.shtml')

#r.encoding = r.apparent_encoding
soup = bs4.BeautifulSoup(r.text, 'html.parser')

ip = soup.find('font', color='blue')
print('どうせ表示されないんだから')
print(ip.text)
