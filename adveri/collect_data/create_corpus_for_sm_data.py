# create for stockmark testデータ
import os
import csv
csv.field_size_limit(1000000000)
import json
import signal
import time
import pandas as pd
from multiprocessing import Process

from modules.scraper import Scraper
from modules.nouns_counter import count_nouns
from modules.corpus import create_corpus

#テストデータ修正
df = pd.read_csv('~/work/git_lab/adveri/existing_random_forest/data/corpus_new_test.tsv', sep='\t', names=['num','cate','text'])

tmp = df[df['text'].isnull()]
tmp['text'] = tmp['cate']
tmp['cate'] = tmp['num']
tmp['num'] = tmp.index

temp = df[~df['text'].isnull()]
temp['num'] = temp.index
df_rev = temp.append(tmp)
df_rev['num'] = df_rev['num'].astype('uint16')
df_rev = df_rev.sort_values('num').reset_index(drop=True)

df_rev.to_csv('./data/data/corpus_20180615_test_revised.tsv', sep='\t', index=False)

#単語分かち書き + count
f_out = open('./data/corpus/corpus_for_testdata_of_stockmark.tsv', 'w')
with open('./data/data/corpus_20180615_test_revised.tsv', 'r') as f_in:
    reader = csv.reader(f_in, delimiter='\t')
    for i, row in enumerate(reader):
        if i%500 == 0:
            print(i)
        row_num = row[0]
        category = row[1]
        text = row[2]
        counter = count_nouns(text)
        f_out.write('\t'.join(map(str,[row_num,category])) + '\t' + json.dumps(counter, ensure_ascii=False) + '\n')

f_out.close()
