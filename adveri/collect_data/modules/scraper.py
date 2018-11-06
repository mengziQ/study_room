# coding: utf-8

import sys
import urllib.request
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString
from janome.tokenizer import Tokenizer
from collections import defaultdict
import copy
import re
import json
import codecs
import time
import requests
from collections import Counter

class Scraper():
    def __init__(self, timeout = 1.):
        self.timeout = timeout
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,ja;q=0.8',
       'Connection': 'keep-alive'}

    def get_html(self, url):
        try:
            try:
                url = url.encode('idna')
            except:
                pass
            source = requests.get(url, headers=self.header, timeout=self.timeout)
            soup = bs(source.text.encode(source.encoding), 'html.parser')
        except EnvironmentError as err:
            print(err)
            # soup = bs('<html></html>', 'html.parser')
            soup = bs('', 'html.parser')
        return soup

    def remove_element(self, soup, tag):
        while soup.find(tag):
            soup.find(tag).decompose()
        return soup

    def remove_unviewable_tag(self, soup):
        values = ['.?display.?:.?none.?', '.?visibility.?:.?hidden.?']
        for value in values:
            while soup.find(attrs={'style':re.compile(value, flags=re.IGNORECASE)}):
                soup.find(attrs={'style':re.compile(value, flags=re.IGNORECASE)}).decompose()
        return soup

    def get_body_texts(self, soup, tags_to_remove = []):

        # scriptタグ / noscriptタグは除外
        for tag in tags_to_remove + ['script', 'noscript', 'style']:
            soup = self.remove_element(soup, tag)

        # unviewableなタグを除外
        soup = self.remove_unviewable_tag(soup)

        texts = ''

        while soup.find(['article', 'section']):
            element = soup.find(['article', 'section']).extract()
            texts += element.getText()

        if not texts:
            texts += soup.getText()

        texts = texts.replace('\n', '').replace('\r', '')
        return texts

    def get_meta_keywords(self, soup):
        contents = soup.findAll(attrs={'name':['KEYWORDS', 'Keywords', 'keywords']})
        if not contents:
           return ''

        keywords = contents[0]['content']
        keywords = keywords.replace(',', '。')
        keywords = keywords.replace('\t', '。')
        return keywords

    def get_words(self, url):
        soup = self.get_html(url)
        meta_kws = self.get_meta_keywords(soup)
        soup = self.remove_element(soup, ['header', 'footer', 'a', 'li'])
        texts = self.get_body_texts(soup)
        return texts + meta_kws

    def export_counter(self, url, path):
        counter = self.count_words(url)
        f = codecs.open(path, 'a', 'utf-8')
        json_text = json.dumps(counter, ensure_ascii=False)
        f.write(url + '\t' + json_text + '\n')

if __name__ == '__main__':
    webtext = Scraper()
    url = 'http://www.nikkei.com/article/DGXMZO05306370X20C16A7000000/?dg=1'
    url = sys.argv[1]
    html = webtext.get_html(url)
    texts = webtext.get_words(url)
    print(texts)
    # keywords = webtext.get_meta_keywords(html)
    # print(keywords)
    # start = time.time()
    # print(webtext.get_words(url))
    # print('execute time : {0:.3f}'.format(time.time()-start))
    # html = webtext.get_html('http://kazunori-yoshimura.co.jp')
