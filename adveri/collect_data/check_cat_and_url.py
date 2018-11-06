import csv
import sys

with open('/home/moeko-asano/adveli_cp/collect_data/data/url_list/url_list_by_bing_201804.tsv', 'r') as url_li:
    objs = url_li.readlines()
    cat = ''
    url_list = []

    for i, o in enumerate(objs):
        print('iter: ', i)
        splited = []
        splited = o.split('\t')
        if i != 0:
            cat_now = splited[1] 
            print(cat_now)
            if cat == cat_now and splited[0] in url_list:
                print('url重複: {}'.format(splited[0]))
                sys.exit()
            elif cat != cat_now:
                cat = cat_now
                print('cat: ', cat)
                url_list = []
                url_list.append(splited[0])
            else:
                url_list.append(splited[0])
        elif i == 0:
            cat = splited[1]
            print('cat:', cat)
            url_list.append(splited[0])
