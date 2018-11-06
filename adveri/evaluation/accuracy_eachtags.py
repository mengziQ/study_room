import numpy as np
import json
import csv
import sys

csv.field_size_limit(sys.maxsize)

j_file = open('../data/id2option.json', 'r')
cat_dict = json.load(j_file)
cat_list = cat_dict.values()
print(cat_list)

out_file = open('./accuracy_eachtag/accuracy_eachtags_model12_精査.txt', 'w')

for cat in cat_list:
    print('now cat:', cat)
    if cat == '違法ダウンロード':
        #cat = 'ネガティブ'
        continue
    elif cat == '2chまとめ' or cat == 'ポイントサイト':
        continue


    predicted = open('./predict_model12_精査.txt', 'r')
    test_data = open('../../data/menu/corpus_201801-06_a.tsv', 'r')
            
    label_list = []
            
    ans = predicted.readlines()
    #test = test_data.readlines()
    #test = csv.reader(test_data, delimiter='\t')
    test = csv.reader((line.replace('\0', '') for line in test_data), delimiter='\t')

    correct = 0
    cnt = 0
    
    for a, t in zip(ans, test):
        pred_list = []
        print('now iter: ', cnt)

        #a = a.replace(',', '').replace('\n', '')
        a = a.split(',')[0].split(' ')[0]
        #pred_list.append(a)
        # fasttext用
        '''
        con_idx = t.find(',')
        label = t[:con_idx]
        label = label.replace('\n', '').replace('__label__', '')
        '''

        label = t[1]

        print('予測値: ', a)
        print('正解: ', label)
        if a == label:
            print('a == label')
            
        # カテゴリ毎の正解率の分母
        #if label != '__label__{}'.format(cat):
        if label != cat:
            #print(label)
            #cnt += 1
            print('continue')
            continue
        '''   
        if len(pred_list) == 2 and label in pred_list:
            correct += 1
            print('どちらか正解！')
        '''
        if a == label:
            #if a == label and label == 'アダルト':
            correct += 1
            print('カテゴリ正解!')
            #elif a == label:
            #   print('正解!')
        else:
            print('不正解!')
            with open('incorrect_data.txt', 'a') as incorrect:
                incorrect.write('{}行目  予測値:{}  正解: {}'.format(cnt, a, label) + '\n')

        cnt += 1

    out_file.write('correct: {}'.format(correct) + '\n')
    out_file.write('cnt: {}'.format(cnt) + '\n')
    print(cat)
    accuracy = correct / cnt
    out_file.write('{} 正解率: {}'.format(cat, accuracy) + '\n')
