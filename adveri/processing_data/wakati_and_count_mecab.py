# random forest学習用のデータ作成の前に、元データをlibSVM形式にするスクリプト
import MeCab
import csv
import sys
import re

csv.field_size_limit(sys.maxsize)

with open('../data/corpus_20180615_test.tsv', 'r') as tsv_file:
    with open('./misc/corpus_for_rf_test.tsv', 'w') as out_f:
        tsv = csv.reader(tsv_file, delimiter='\t')
        for i, t in enumerate(tsv):
            #if i == 17:
             #   sys.exit()
            print('now iter: ', i)
            word_dic = {}
            label = t[0]
            input = t[1]
            mt = MeCab.Tagger('-Ochasen -d /home/moeko-asano/mecab-ipadic-neologd/build/mecab-ipadic-2.7.0-20070801-neologd-20180419/')
            
            # 取得できるはずの文字がエンコードエラーになるバグへの暫定的な対応として空文字をパースする
            mt.parse('')

            node = mt.parseToNode(input)

            while node:
                try:
                    if word_dic.get(node.surface) is None:
                        #print('辞書追加')
                        word_dic[node.surface] = 1
                    else:
                        #print('カウント追加')
                        word_dic[node.surface] += 1
                    #print(node.surface)
                except Exception as e:
                    print(e)

                node = node.next
            
            st = label + '\t' + '{'

            for w, c in word_dic.items():
                if re.match(r'\s+' , w):
                    continue
                st += '"' + w + '"' + ':' + str(c) + ', '
                    
                
            st = st[:-2] + '}'
            out_f.write(st + '\n')



