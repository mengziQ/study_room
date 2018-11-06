#coding:utf-8
import requests
import json
import csv
csv.field_size_limit(1000000000)
import re
#import pandas as pd
import codecs
import sys


url = "http://54.65.61.104:57772/api/iknow/v1/USER/highlight?CacheUserName=SuperUser&CachePassword=cache2017"

def func(text,sentence):
    if sentence == 1:
        highlight = [{'style':"[]", 'role':"concept"},\
                     {'style':"<>", 'role':"relation"},\
                     {'style':"{}", 'role':"nonRelevant"}]
    else:
        highlight = [{'style':"[]", 'role':"concept"}]
        params = {'text': text, 'configuration':'ja', 'highlight':highlight}
        headers = {'accepts':'application/json'}
        res = requests.post(url, data = json.dumps(params), headers = headers)
    return res

f_out = open('./misc/corpus_20180615_train_inter.tsv', 'w')

"""
ex_url = []
with open('./data/intersys/dataset_for_contents_match.tsv', 'r') as f_in:
    reader = csv.reader(f_in, delimiter='\t')
    for row in reader:
        ex_url.append(row[0])
"""

with open('../data/corpus_20180615_train.tsv', 'r') as f:
    reader = csv.reader(f,delimiter='\t')
    #header = next(reader)
    regex = re.compile(r'\[(.+?)\]')
    for i,row in enumerate(reader):
        if i %100 == 0:
            print('iter',i)
        #if (row[0] in ex_url):
        #    continue
        try:
            #res = func(row[3],2)
            res = func(row[1], 2)
            tmp = res.json()
            match = regex.findall(tmp['text'])
            #f_out.write('\t'.join(map(str,[row[1],row[2],' '.join(match)])) + '\n')
            f_out.write('\t'.join(map(str,[row[0],' '.join(match)])) + '\n')
        except Exception as e:
            print('%r' % e)
                                                                                                                                                                                                                      
f_out.close()
