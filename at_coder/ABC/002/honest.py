m1, m2 = input().split(' ')
if 0 > int(m1) or  int(m1) > pow(10, 9) or 0 > int(m2) or int(m2) > pow(10, 9):
  print('入力値は0〜10の9乗までです')
  exit()

if int(m1) > int(m2):
  print(m1)
else:
  print(m2)

