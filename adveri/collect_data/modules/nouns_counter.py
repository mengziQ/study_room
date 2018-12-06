# coding : utf-8

import re
from janome.tokenizer import Tokenizer
from collections import Counter

'''
    token.surface,                        # 表層形
    token.part_of_speech.split(',')[0],   # 品詞
    token.part_of_speech.split(',')[1],   # 品詞細分類1
    token.part_of_speech.split(',')[2],   # 品詞細分類2
    token.part_of_speech.split(',')[3],   # 品詞細分類3
    token.infl_type,                      # 活用型
    token.infl_form,                      # 活用形
    token.base_form,                      # 原形
    token.reading,                        # 読み
    token.phonetic,                       # 発音
'''

def tokenize(texts):
    t = Tokenizer()
    return t.tokenize(texts)

def is_noun(token):
    if token.part_of_speech.split(',')[0] == '名詞':
        return True
    else:
        return False

def is_normal_noun(token):
    if '一般' in token.part_of_speech:
        return True
    else:
        return False

def is_potential_adverb(token):
    if token.part_of_speech.split(',')[1] == '副詞可能':
        return True
    else:
        return False

def is_proper_noun(token):
    if token.part_of_speech.split(',')[1] == '固有名詞':
        return True
    else:
        return False

def is_number(token):
    if token.part_of_speech.split(',')[1] == '数':
        return True
    else:
        return False

def is_pronoun(token):
    if token.part_of_speech.split(',')[1] == '代名詞':
        return True
    else:
        return False

def is_in_dictionary(token):
    # 読み方がわからない = 日本語以外の言語
    if token.reading == '*':
        return False
    else:
        return True

def is_one_hiragana(token):
    if len(token.surface) == 1 and re.search('[ぁ-んァ-ン]', token.surface):
        return True
    else:
        return False

def is_number_plus_TSU(token):
    # 一つ、二つ、三つ、〜 九つであるかどうかを判断する
    if re.search('[一二三四五六七八九]つ', token.surface):
        return True
    else:
        return False

def check_to_adopt(token):
    if not is_noun(token):
        return False

    if not is_normal_noun(token):
        return False

    if is_pronoun(token):
        return False

    # if not is_potential_adverb(token):
    #     return False

    # if not is_proper_noun(token):
    #     return False

    if is_one_hiragana(token):
        return False

    if not is_in_dictionary(token):
        return False

    if is_number_plus_TSU(token):
        return False

    return True

def count_nouns(texts):
    tokens = tokenize(texts)
    words = []

    for token in tokens:
        if check_to_adopt(token):
            words.append(token.base_form)
    return dict(Counter(words))


# def _count_nouns(self, texts):
#     words = []
# 
#     t = Tokenizer()
#     try:
#         tokens = t.tokenize(texts)
#     except:
#         tokens = []
#     for token in tokens:
#         # 数詞は除外する
#         if token.part_of_speech.split(',')[1]  == u'数':
#             continue
#         # 読み方がわからないものは除外（英語等）
#         elif token.reading  == u'*':
#             continue
#         # 名詞だけピックアップ
#         elif token.part_of_speech.split(',')[0] in [u'名詞']:
#             if token.base_form == u'*':
#                 word = token.surface
#             else:
#                 word = token.base_form
#             words.append(word)
#     return dict(Counter(words))

if __name__ == '__main__':
    texts = 'アメリカ'
    print(tokenize(texts)[0].part_of_speech)
