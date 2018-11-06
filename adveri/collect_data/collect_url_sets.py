# coding:utf-8

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/modules')

from modules.bing import Bing

n_url_per_category = 150
f_out = './data/url_list/url_list_illegal.csv'

bing = Bing(api_key='5b5e82f51bfc449c987bbfb8ea727c0c')

def get_search_words(file_path):
    words = open(file_path, 'r').read()
    return list(filter(None, words.split('\n')))

def get_urls(words, news, adults):
    urls = []
    for word in words:
        print(word)
        urls += [elem['url'] for elem in bing.web_search(query=word, \
            num_of_results=int(n_url_per_category / len(words)), keys=['url'], News=news, Adults=adults)]
        #urls += [elem['url'] for elem in bing.web_search(query=word, num_of_results= 1, keys=['url'], News=news, Adults=adults)]
        print(urls)
    return urls

def main():
    # 検索ワードの読み込み
    #paras = {'アダルト' : {'file_path' : './data/search_words/adults.csv', 'News':False, 'Adults':True},
           # 'ネガティブ' : {'file_path' : './data/search_words/negative.csv', 'News':True, 'Adults':True},
           # 'アルコール' : {'file_path' : './data/search_words/alchol.csv', 'News':False, 'Adults':False},
           # 'たばこ' : {'file_path' : './data/search_words/tabacco.csv', 'News':False, 'Adults':False},
           # '百貨店' : {'file_path' : './data/search_words/department.csv', 'News':False, 'Adults':False},
           # 'スーパー' : {'file_path' : './data/search_words/supermarket.csv', 'News':False, 'Adults':False}}
    paras = {'違法ダウンロード' : {'file_path' : './data/search_words/illegal_download_bk.csv', 'News':False, 'Adults':False}}

    # bing APIを実行し、URLをファイルに書き込み
    with open(f_out, 'a') as f:
        for category, info in paras.items():

            words = get_search_words(info['file_path'])
            urls = get_urls(words, info['News'], info['Adults'])

            for url in urls:
                f.write('\t'.join([url, category]) + '\n')

if __name__ == '__main__':
    main()
