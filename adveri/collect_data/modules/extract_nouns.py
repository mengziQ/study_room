from nouns_counter import count_nouns
import csv 
import sys
import json

csv.field_size_limit(sys.maxsize)

with open('/home/moeko-asano/jupyter/git_lab/adveri/existing_random_forest/data/corpus_new_negative.tsv', 'r') as r:
    reader = csv.reader((line.replace('\0', '') for line in r), delimiter='\t')

    out_f = open('/home/moeko-asano/jupyter/git_lab/adveri/existing_random_forest/processing_data/misc/corpus_new_negative_svm.tsv', 'w')
    for i, o in enumerate(reader):
        print('iter: ', i)
        #if i == 850:
           # sys.exit()
        counter = count_nouns(o[3])
        out_f.write('\t'.join([o[0], o[1], o[2]]) + '\t' + json.dumps(counter, ensure_ascii=False) + '\n')

