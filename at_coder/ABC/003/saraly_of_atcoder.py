task = input()

if 4 > int(task) or 100 < int(task):
  print('タスク数は4以上100以下で入力してください')
  exit

idx = 0
avg_salary = 0

while idx <= int(task):
  avg_salary += 10000 * idx * (1/int(task))
  idx += 1

avg_salary = int(round(avg_salary, 0))

print(str(avg_salary) + '\n')

