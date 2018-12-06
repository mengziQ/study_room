import numpy as np
import csv
import sys

csv.field_size_limit(sys.maxsize) 

with open('./predict_model12_やり直し.txt', 'r') as predicted:
    with open('../data/corpus_20180615_test_bk.tsv', 'r') as test_data:
        ans = predicted.readlines()
        #test = test_data.readlines()
        test = csv.reader(test_data, delimiter='\t')
        correct = 0
        cnt = 0
        for a, t in zip(ans, test):
            print('now iter: ', cnt)
            ans_list = []
            if ',' in a:
                splited = a.split(',')
                ans_list = splited
            a = a.replace(',', '').replace('\n', '')
            #con_idx = t.find(',')
            #label = t[:con_idx]
            #label = label.replace('\n', '')#.replace('__label__', '')
            label = t[0]
            print('ans_list:', ans_list)
            print('予測値a: ', a)
            print('正解: ', label)
            
            if len(ans_list) > 0:
                for an in ans_list:
                    if an.replace('\n', '') == label:
                        correct += 1
                        print('どちらか正解!')
            elif a == label:
                correct += 1
                print('正解!')
            else:
                print('不正解!')
                with open('incorrect_data.txt', 'a') as incorrect:
                    incorrect.write('{}行目  予測値:{}  正解: {}'.format(cnt, a, label) + '\n')

            cnt += 1

        print('correct: ', correct)
        print('cnt: ', cnt)
        accuracy = correct / cnt
        print('正解率: ', accuracy)
