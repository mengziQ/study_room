n, s, t = map(int, input().split())
w = int(input())

cnt = 0
if s <= n <= t:
  cnt += 1

for i in range(n - 1):
  if s <= (w + int(input())) <= t:
    cnt+= 1

print(cnt)
