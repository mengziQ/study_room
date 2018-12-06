import re

s = input()
r = input()

repatter = re.compile(r)
result = repatter.findall(s)

if len(result) == 0:
  print('-1')
else: 
  print(len(max(result, key=len)))

