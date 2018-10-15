a, b, c, k = map(int, input().split())
s, t = map(int, input().split())

if s + t >= k:
  print(s * (a - c) + t * (b - c))
else:
  print(s * a + t * b)
