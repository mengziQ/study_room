# Ice Tea Store
input_line1 = input()
input_line2 = input()

price_list = []

try:
  # ４つ数字を入力しなかったときのためにtryブロックで囲む
  price_list = list(map(int, input_line1.split(' ')))
  for p in price_list:
    if 1 > p or p > pow(10, 8):
      print('アイスティーの値段は1〜10^8までです')
      exit()

except Exception as e:
  print(e)
  exit()

#print(len(price_list))

if 1 > int(input_line2) or int(input_line2) > pow(10, 9): 
  print('買えるアイスティーの量は1〜10^9までです')
  exit()

n = int(input_line2)

cost = 0

if n/2 >= 1:
  min2 = min([price_list[0]*8, price_list[1]*4, price_list[2]*2, price_list[3]])
  #print('min2', min2)
  cost = min2 * int(n/2)
  #print('2L通過時のコスト:', cost)  
  n = n - 2 * int(n/2)

if n/1 >= 1:
  min1 = min([price_list[0]*4, price_list[1]*2, price_list[2]])
  cost = cost + min1 * int(n/1)
  #print('1L通過時のコスト', cost)
  n = n - 1 * int(n/1)

if n/0.5 >= 1:
  min_half = min([price_list[0]*2, price_list[1]])
  cost = cost + min_half * int(n/0.5)
  #print('0.5L通過時のコスト' , cost)
  n = n - 0.5 * int(n/0.5)

if n/0.25 >= 1:
  cost = cost + price_list[0] * int(n/0.25)
  #print('0.25L通過時のコスト', cost)

print(cost)



