with open('a.txt', 'r') as a:
  lines = a.readlines()
  
  event = []
  finished = []

  #with open('yahoo_ss_acountid.txt','r') as c:
   # c.readlines()
    #finished.append(c)

  for line in lines:
    if line not in event:
      event.append(line)

with open('c.txt', 'w') as b:
  b.writelines(event)

