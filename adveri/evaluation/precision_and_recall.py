import csv
import sys
import glob
import json

csv.field_size_limit(sys.maxsize)

id2option = json.load(open('../convert_to_sparse/map/id2option_bk2.json', 'r'))

out_f = open('./precision_and_recall/retrain_old_test2.tsv', 'w')

for name in glob.glob('./csv/retrain_old_test/*.txt'):
    cat = name.split('/')[-1].replace('.txt','')
    if cat == '食品・飲料・日用品':
        cat = '食品・飲料/日用品'
    print(cat)
    for k, v in id2option.items():
        #if cat == 'ネガティブ':
         #   id_option = '24'
          #  break
        if v == cat:
            id_option = k

    in_f = open(name, 'r')
    obj = csv.reader(in_f, delimiter='\t')
    
    cnt = 0
    posi = 0
    nega = 0
    precision = 0.0
    recall = 0.0

    # 正解カテゴリ情報入手のために読み込み
    data_file = open('./predict/predict_model8_retrain_old_test.tsv', 'r')
    obj2 = csv.reader((line.replace('\0', '') for line in data_file), delimiter='\t') 

    for o, o2 in zip(obj, obj2):
        #if len(o) < 4:
         #   continue
        #if o[1] == id_option:
       
        if id_option == o2[1]: 
            cnt += 1
       
        if id_option == o2[1] and o[2] == '1':
            posi += 1

        if id_option != o2[1] and o[2] == '1' and o2[1] != '2chまとめ' and o2[1] != 'ポイントサイト':
            nega += 1
        

    if posi+nega != 0:
        precision = posi/(posi+nega)
        recall = posi/cnt

    out_f.write('\t'.join([cat, str(posi), str(nega), str(cnt), str(precision), str(recall)]) + '\n')
    
