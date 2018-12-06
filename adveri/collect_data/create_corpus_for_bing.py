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

#f_url_list_prism3 = './data/url_list/url_list_prism3.tsv'
f_url_list_bing = './data/url_list/urllist_2ch_after.tsv'
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
        #print('{}回目'.format(i))
        if not (i >= n_start and i < n_end):
            continue

        url = r[0]
        category = r[1]

        if i % 100 == 0:
            print('iter : ', i)

        counter = create_corpus(url)
        #print(counter)
        if not counter:
            continue
        # 「url  カテゴリ　コーパス」を書き込むように変更
        f_out.write('\t'.join(['N' + "{0:06d}".format(i), url, category, counter]) + '\n')
        #f_out.write('\t'.join([url, category]) + '\t' + json.dumps(counter, ensure_ascii=False) + '\n')

    f_in.close()
    f_out.close()

def main():
    jobs = [
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus15.tsv', 0, 30000)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus16.tsv', 30001, 60000)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus17.tsv', 60001, 90000)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus18.tsv', 90001, 120000)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus19.tsv', 120001, 150000)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus20.tsv', 150001, 180000)),
        Process(target=create_part_corpus, args=(f_url_list_bing, 'tmp/corpus21.tsv', 180001, 202670))
    ]
    
    start_time = time.time()
    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    finish_time = time.time()
    print(finish_time - start_time)


def append_data():
    f_out = open(f_corpus_path + 'corpus_2ch_domain_check.tsv', 'w')
    for i in range(15, 21):
        f_in = open(f_corpus_path + 'tmp/corpus{}.tsv'.format(i), 'r')
        
        f_out.write(f_in.read())

    f_out.close()

if __name__ == '__main__':
    main()
    append_data()
