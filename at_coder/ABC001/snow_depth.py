h1 = int(input())
h2 = int(input())

if 0 > h1 or 2000 < h1 or 0 > h2 or 2000 < h2:
  print('値は0〜2000の間で入力してください')
  exit()

print(str(h1 - h2) + '\n')

