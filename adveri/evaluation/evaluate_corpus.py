# coding: utf-8

import numpy as np
import pandas as pd
import time, sys, json
from sklearn.externals import joblib
from modules.scraper import Scraper
from modules.nouns_counter import count_nouns
from modules.corpus import create_corpus
import csv
import sys

csv.field_size_limit(sys.maxsize)

scraper = Scraper()

targets = {'0': 0.03742972823395765, '31': 0.021511170662083832, '32': 0.020346042934956746, '11': 0.019603274008913228, '23': 0.01865660773062247, '16': 0.021802452593865602, '4': 0.005519792607264571, '45': 0.013486353441496023, '6': 0.023797733826570737, '20': 0.01620983950365559, '30': 0.021307273309836592, '33': 0.02317147767323993, '29': 0.018175992543182546, '42': 0.02202091404270193, '19': 0.024977425650286912, '13': 0.011709533657627218, '36': 0.02232676007107279, '41': 0.023957938889050713, '27': 0.0197634790713932, '40': 0.01996737642364044, '22': 0.01999650461681862, '7': 0.02162768343479654, '37': 0.02069558125309487, '47': 0.023855990212927093, '44': 0.01955958171914596, '39': 0.021103375957589352, '28': 0.01720019807171361, '34': 0.016573941918382802, '12': 0.014214558270950453, '26': 0.02020040196906586, '10': 0.024132708048119775, '35': 0.019341120270309632, '43': 0.02172963211092016, '24': 0.017156505781946347, '8': 0.021117940054178438, '46': 0.02419096443447613, '25': 0.02181701669045469, '9': 0.023681221053858028, '21': 0.018161428446593457, '15': 0.018088607963648015, '18': 0.0151757886458303, '5': 0.024001631178817977, '17': 0.017360403134193587, '1': 0.024758964201450583, '3': 0.019020710145349683, '14': 0.018307069412484344, '48': 0.023695785150447117, '2': 0.0224432728437855, '38': 0.025064810229821443}
targets = pd.DataFrame.from_dict(targets, orient='index')

if __name__ == '__main__':
    with open('predict_retrain_2ch_revise.tsv', 'w') as out_f:
        with open('../data/2ch_all_data.tsv', 'r') as corp:
            #assert len(sys.argv) == 2, 'Invalid length of arguments. Only one argument is needed.'
            clf = joblib.load('../create_model/models/depth_90/rf_model8_retrain.pkl')
            #url = sys.argv[1]
            
            id2word = json.load(open('../convert_to_sparse/map/id2feature_model8_retrain.json', 'r'))
            word2id = {word:int(id) for id, word in id2word.items()}
            
            obj = csv.reader((line.replace('\0', '') for line in corp), delimiter='\t')

            for z, o in enumerate(obj):
                if z == 0:
                    continue
                corpus = count_nouns(o[2])
                n_word = sum(corpus.values())
                
                features = [(id, corpus[w] / n_word) if w in corpus.keys() else (id, 0)  for w, id in word2id.items()]
                features = pd.DataFrame.from_dict(dict(features), orient='index')
                
                pred = pd.DataFrame(np.transpose(clf.predict_proba(features.transpose())))
                pred.index = list(map(str, pred.index))
                pred = pd.merge(pred, targets, left_index=True, right_index=True)
                pred['lift'] = pred.iloc[:,0] / (1 - pred.iloc[:,0]) / (pred.iloc[:,1] / (1 - pred.iloc[:,1]))
                # lift列でソート
                #pred.sort_values('lift', ascending=False, inplace=True)
                # rfスコア(0_x列)でソート
                #pred.sort_values('0_x', ascending=False, inplace=True)
                #print(pred['0_x'])

                id2target = json.load(open('../convert_to_sparse/map/id2option.json', 'r'))
                """
                for i in range(3):
                    category = id2target[str(pred.index[i])]
                    lift = pred.iloc[i, 2]
                    
                    if lift < 1.:
                        break
                """ 
                    #print('{} : {}'.format(category, score))
                
                option2f = json.load(open('../convert_to_sparse/map/option2target.json', 'r'))

                for e, i in enumerate(pred.index):
                    #category = id2target[str(pred.index[0])]
                    category = id2target[str(i)]
                    rfscore = pred.iloc[e, 0]
                    #print(rfscore)
                    if e == 0:
											  # domain
                        sp = o[1].split('/')
                        domain = '/'.join([sp[0], sp[1], sp[2]])
                        out_f.write('\t'.join([o[0], o[1], domain, category,  str(rfscore)]) + '\t')
                    elif e == len(pred.index) - 1:
                    #elif e == 1:
                        #out_f.write(category + ' ' + str(rfscore) + '\n')
                        out_f.write('\t'.join([category, str(rfscore)]) + '\n')
                    
                    else:
                        #out_f.write(category + ' ' + str(rfscore) + ',  ')
                        out_f.write('\t'.join([category, str(rfscore)]) + '\t')
                    
