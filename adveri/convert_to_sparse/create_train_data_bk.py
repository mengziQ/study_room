# coding :utf-8

import os
import csv
from ast import literal_eval
import json
import numpy as np
from datetime import date
from collections import Counter
from itertools import chain, product
from modules.dAIC import calc_diff_aic


def _create_data_for_dAIC(filename):
    ## Reference:
    ## https://www.dynacom.co.jp/product_service/packages/snpalyze/sa_t2_aic-cont.html

    true_positive = {}
    true = {}
    positive = {}

    f = open(filename, 'r')
    reader = csv.reader(f, delimiter='\t')
    header = next(reader)

    # create true-positive and true
    # At first, append words per doc.
    # Second, count docs with a word by Counter.
    for r in reader:
        url = r[0]
        cate = r[1]
        words = literal_eval(r[2])

        # initialize
        if not cate in true_positive.keys():
            true_positive[cate] = []
        if not cate in true.keys():
            true[cate] = 0

        true_positive[cate] += words.keys()
        true[cate] += 1

    for cate in true_positive.keys():
        true_positive[cate] = Counter(true_positive[cate])

    # create positive
    for cate, words in true_positive.items():
        for word, tp in words.items():

            # initialize
            if not word in positive.keys():
                positive[word] = 0

            positive[word] += tp

    # count the number of docs
    n_all = sum(true.values())

    return true_positive, true, positive, n_all


def calc_dAIC(filename):
    true_positive, true, positive, n_all = _create_data_for_dAIC(filename)
    weights = {}
    for category, word in product(true.keys(), positive.keys()):
        if not category in weights.keys():
            weights[category] = {}
        weights[category][word] = \
            calc_diff_aic(true_positive[category][word], \
                true[category], \
                positive[word], \
                n_all)
    return weights

# select features in order from the smallest dAIC for every target..
def select_features(filename, num=500):
    weights = calc_dAIC(filename)
    features = {}
    for category in weights.keys():
        words = sorted(weights[category].items(), key=lambda x:x[1])[:num]
        features[category] = [word[0] for word in words]

    return features


if __name__ == '__main__':

    # Load data.
    filename = '../collect_data/data/corpus/corpus.tsv'
    features = list(set(chain.from_iterable(select_features(filename, num=3000).values())))

    id2target = json.load(open('./map/id2target.json', 'r'))
    target2id = {target:id for id, target in id2target.items()}

    id2word = {id:word for id, word in enumerate(features)}
    word2id = {word:id for id, word in id2word.items()}

    reader = csv.reader(open(filename, 'r'), delimiter='\t')

    # Open files to export results into.
    f_id2word = open('./map/id2feature.json', 'w')
    json.dump(id2word, f_id2word)

    f_urls_train = open('./data/urls_train.csv', 'w')
    f_urls_test = open('./data/urls_test.csv', 'w')
    f_out_train = open('./data/sparse_data_train.txt', 'w')
    f_out_test = open('./data/sparse_data_test.txt', 'w')

    # Write
    for i, r in enumerate(reader):
        if i % 1000 == 0:
            print('iter : ', i)
        url = r[0]
        target = r[1]
        corpus = literal_eval(r[2])
        corpus = {word : float(value) / sum(corpus.values()) for word, value in corpus.items()}

        corpus = [(word2id[word], value) for word, value in corpus.items() if word in word2id.keys()]
        corpus.sort()
        corpus = [str(id) + ':' +  str(value) for id, value in corpus]

        if i % 10:
            f_urls_train.write(url + '\n')
            f_out_train.write(target2id[target] + ' ' + ' '.join(corpus) + '\n')
        else:
            f_urls_test.write(url + '\n')
            f_out_test.write(target2id[target] + ' ' + ' '.join(corpus) + '\n')


    # Close files.
    f_urls_train.close()
    f_urls_test.close()
    f_out_train.close()
    f_out_test.close()

