# coding: utf-8

import os
import csv
import json
import signal
import time
from multiprocessing import Process

from modules.scraper import Scraper
from modules.nouns_counter import count_nouns
from modules.corpus import create_corpus

# path_to_import = './data/url_list/'
# path_to_export = './data/corpus/'
# files = os.listdir(path)

f_url_list_prism3 = './data/url_list/url_list_prism3.tsv'
f_url_list_bing = './data/url_list/url_list_by_bing.tsv'
f_corpus_path = './data/corpus/'

scraper = Scraper()

def signal_handler(signum, frame):
    raise Exception("end of time")

def create_part_corpus(f_url_list, f_corpus, n_start=0, n_end=10000000000):

    f_in = open(f_url_list, 'r')
    reader = csv.reader(f_in, delimiter='\t')
    header = next(reader)

    f_out = open(f_corpus_path + f_corpus, 'a')

    for i, r in enumerate(reader):
        if not (i >= n_start and i < n_end):
            continue

        url = r[0]
        category = r[1]

        if i % 100 == 0:
            print('iter : ', i)

        counter = create_corpus(url)
        if not counter:
            continue
        f_out.write('\t'.join([url, category]) + '\t' + json.dumps(counter, ensure_ascii=False) + '\n')

    f_in.close()
    f_out.close()

def main():
    jobs = [
        Process(target=create_part_corpus, args=(f_url_list_prism3, 'tmp/corpus1.tsv', 0, 15000)),
        Process(target=create_part_corpus, args=(f_url_list_prism3, 'tmp/corpus2.tsv', 15000, 30000)),
        Process(target=create_part_corpus, args=(f_url_list_prism3, 'tmp/corpus3.tsv', 30000, 45000)),
        Process(target=create_part_corpus, args=(f_url_list_prism3, 'tmp/corpus4.tsv', 45000, 60000)),
        Process(target=create_part_corpus, args=(f_url_list_prism3, 'tmp/corpus5.tsv', 60000, 75000)),
        Process(target=create_part_corpus, args=(f_url_list_prism3, 'tmp/corpus6.tsv', 75000, 82953)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus7.tsv', 0, 300000))
    ]

    start_time = time.time()
    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    finish_time = time.time()
    print(finish_time - start_time)


def append_data():
    f_out = open(f_corpus_path + 'corpus.tsv', 'w')
    for i in range(1, 8):
        f_in = open(f_corpus_path + 'tmp/corpus{}.tsv'.format(i), 'r')
        f_out.write(f_in.read())

    f_out.close()

if __name__ == '__main__':
    main()
    append_data()
