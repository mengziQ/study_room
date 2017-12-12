task = int(input())

salary = 0

# for文を使う。インクリメントは書かなくても大丈夫。in句の後はlenではなくrangeでないといけない。
# in句の後は、int型ではなくリストでないといけないから。
for i in range(task + 1):
  salary += int(i * 10000)

salary = int(salary / task)

print(salary)

