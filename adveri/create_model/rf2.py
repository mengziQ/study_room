# coding :utf-8

import os
import time
import scipy
from sklearn.datasets import load_svmlight_file
from sklearn.datasets import load_svmlight_files
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.externals import joblib

if __name__ == '__main__':

    for f in ['train_log8_retrain.txt', 'test_log8_retrain.txt']:
        if f in os.listdir('./'):
            os.remove(f)

    for d in [10, 20, 30, 40, 50, 60, 70, 80, 90,100]:
        path = './models/'
        dir_name = 'depth_{}'.format(d)
        if not(dir_name in os.listdir(path)):
            os.mkdir(path + dir_name)

        # 学習データの特徴量の次元数がテストデータより1つ大きくなってしまうエラーへの対応のため、学習データとテストデータを一緒にロード
        X_train, y_train, X_test, y_test = load_svmlight_files(['../convert_to_sparse/misc/sparse_data_train_retrain.txt', '../convert_to_sparse/misc/sparse_data_test_retrain.txt'])
        print(set(y_train))
        print(set(y_test))

        #X_train, y_train = load_svmlight_file('../convert_to_sparse/misc/sparse_data_train_nouns.txt')
        clf = RandomForestClassifier(n_estimators=200, random_state=1, verbose=True, max_depth=d)

        print('start modeling')
        print(d)
        start_time = time.time()
        clf = clf.fit(X_train, y_train)
        joblib.dump(clf, path + dir_name + '/rf_model8_retrain.pkl')

        print('finish modeling!')
        print('exec time : {}'.format(time.time() - start_time))

        #X_test, y_test = load_svmlight_file('../convert_to_sparse/misc/sparse_data_test_nouns.txt')
        predicted_train = clf.predict_proba(X_train)
        predicted_test = clf.predict_proba(X_test)

        # for data in [y_train, y_test]:
        for j, (data, pre, f_name) in enumerate([(y_train, predicted_train, 'train_log8_retrain.txt'), (y_test, predicted_test, 'test_log8_retrain.txt')]):
            if not f_name in os.listdir('./'):
                f = open(f_name, 'w')
            else:
                f = open(f_name, 'a')

            f.write('\ndepth : {}\n'.format(d))
            #print('data: ', set(data))
            #print('pre: ', pre)
            for i in sorted(set(data)):
                i = int(i) 
                y_flg = [1 if value == i else 0 for value in data]
                #print('i: ', i ) 
                #print('y_flg: ', y_flg)
                #print('pre[:, i]: ', pre[:, i])
                fpr, tpr, thresholds = metrics.roc_curve(y_flg, pre[:, i])
                auc = metrics.auc(fpr, tpr)
                f.write('category : {}, auc : {}\n'.format(i, auc))
