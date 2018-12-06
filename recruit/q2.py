import sys

q_file = sys.argv[1]
dic_file = sys.argv[2]

alp_dic = {}
bl_dic = {'a':'A', 'b':'B', }

q_dic = {}
d_dic = {}

# 暗号文を辞書化(やっぱリストにしようかな・・・)
with open(q_file, 'r') as question:
  q_words = question.read()

  for qw in q_words.split():
    if q_dic.get(len(qw)) is None:
      q_dic[len(qw)] = [qw]
    elif qw not in q_dic[len(qw)]:
      q_dic[len(qw)].append(qw)

# 辞書を辞書化
with open(dic_file, 'r') as dic:
  d_words = dic.read()

  for dw in d_words.split():
    if d_dic.get(len(dw)) is None:
      d_dic[len(dw)] = [dw]
    elif dw not in d_dic[len(dw)]:
      d_dic[len(dw)].append(dw)
  
# 分布調査用
for k, v in d_dic.items():
  print(str(k) + ' : ' + str(len(v)) + '\n')
# 終

# 1文字の単語
#alp_dic[d_dic[1][0]] = q_dic[1][0]

# 2文字の単語
#for two in d_dic[14]:
  #print(two)
