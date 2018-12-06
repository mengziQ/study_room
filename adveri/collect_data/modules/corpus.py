# coding: utf-8

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import signal
from scraper import Scraper
from nouns_counter import count_nouns

scraper = Scraper()

def signal_handler(signum, frame):
    raise Exception("end of time")

def create_corpus(url):
    try:
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(10)
        # テキストそのものを返すように修正
        counter = scraper.get_words(url)
        #counter = count_nouns(texts)
    except Exception as e:
        print(e)
        return {}
    return counter

if __name__ == '__main__':
    url = sys.argv[1]
    print(create_corpus(url))

