k, L, H = map(int, input().split())

dic = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1, 'A':1, 'B':2, 'C':0, 'D':1, 'E':0, 'F':0}
nchar = '0123456789ABCDEF'

cs_sum = 0
for i in range(L, H+1):
  cs = 0
  if k != 10:
    while i > 0:
      remain = nchar[i % k]
      if len(remain) == 1:
        cs += dic[remain]
      else:
        for r in remain:
          cs += dic[r]
      
      i = int(i / k)

  else:
    for num in str(i):
      cs += dic[num]
  
  cs_sum += cs

print(cs_sum)
