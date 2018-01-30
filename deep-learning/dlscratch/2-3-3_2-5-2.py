import numpy as np
import sys

# 同じ処理何回も書いてるけどごめんなさい、直すの面倒

def AND(x):
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum((x * w)) + b

  if tmp <= 0:
    return 0
  elif tmp > 0:
    return 1

def NAND(x):
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum((x * w)) + b

  if tmp <= 0:
    return 0
  elif tmp > 0:
    return 1 

def OR(x):
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum((x * w)) + b

  if tmp <= 0:
    return 0
  elif tmp > 0:
    return 1 

def XOR(x):
  s1 = NAND(x)
  s2 = OR(x)
  x = [s1, s2]
  y = AND(x)
  return y

args = sys.argv
x1, x2 = map(int, input().split(' ')) 
x = np.array([x1, x2])


if args[1] == 'and': 
  print(AND(x))                                                                                                                                                                                     
elif args[1] == 'nand':
  print(NAND(x))
elif args[1] == 'or':
  print(OR(x))
elif args[1] == 'xor':
  print(XOR(x))
