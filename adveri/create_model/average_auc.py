import sys
import numpy as np

with open('test_log8_retrain.txt', 'r') as in_f:
    obj = in_f.readlines()
    score_list = []
    ave_list = []
    for i, o in enumerate(obj): 
        #print('iter: ', i)
        if i != 1 and 'depth' in o :
            avg = np.mean(score_list)
            print(avg)
            ave_list.append(avg)
            score_list = []
        if 'category' in o:
            splited = o.split(',')
            score = splited[1].replace('auc : ', '').replace('\n', '').strip()
            score_list.append(float(score))

    avg = np.mean(score_list)
    ave_list.append(avg)
    print(avg)
    print('depth ', (ave_list.index(max(ave_list)) + 1) * 10)
