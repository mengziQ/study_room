import json
import csv
import sys

csv.field_size_limit(sys.maxsize)

thre_dic = {}
thre_f = open('./threshold/model8_retrain/aaaout_0.90.csv', 'r')
thre = csv.reader(thre_f)
for th in thre:
    thre_dic[th[0]] = float(th[1])

print(thre_dic)

for cat, t in thre_dic.items():
    #print(cat)
    if cat != '2chまとめ':
        continue
    #if cat != '医療・福祉' and cat != '通信・キャリア' and cat != 'エンタメ':
     #   continue
    #if cat ==  '2chまとめ' or cat == 'ポイントサイト': #or cat == 'アダルト' or cat == '通信・キャリア':
     #   continue
    if cat == '食品・飲料/日用品':
        cat_name = '食品・飲料・日用品'
    else:
        cat_name = cat

    in_f = open('./predict/predict_retrain_2ch_revise.tsv', 'r')
    #obj = in_f.readlines()
    obj = csv.reader((line.replace('\0', '') for line in in_f), delimiter='\t')

    out_f = open('./csv/retrain_2ch/90/{}.txt'.format(cat_name), 'w')

    for i,o in enumerate(obj):
        '''
        if i == 5:
            sys.exit()
         
        if o[1] != cat:
            out_f.write(','.join([o[0], '', '']) + '\n')
            continue
        '''
       
        #splited = o.split(',')        

        for e in range(2, len(o)):
        #for e, sp in enumerate(splited):
            if cat == o[e]:
                score = o[e + 1]
                if cat == 'ネガティブ':
                    score = score.replace('\n', '')
                print('score: ', score)
                print('thre_dic[cat]: ', thre_dic[cat])

                # ドメイン
                #domain = o[1].split('/')

                if float(score) >=  thre_dic[cat]:
                    #out_f.write(o[0] + ',' + score  + ',' + '1' + '\n')
                    out_f.write('\t'.join([o[0], o[1], o[2], score, '1']) + '\n')
                else:
                    #out_f.write(o[0] + ',' + score  + ',' + '0' + '\n')
                    out_f.write('\t'.join([o[0], o[1], o[2], score, '0']) + '\n')
                
