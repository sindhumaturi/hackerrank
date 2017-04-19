lst = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    lst.append([name,score])

small = lst[0][1]
for i in lst:
    if (i[1] < small):
        small = i[1]
lst3 = []       
for i in lst:
    if (i[1] != small):
        lst3.append(i)

small = lst3[0][1]
for i in lst3:
    if (i[1] < small):
        small = i[1]
lst2 = []        
for i in lst3:
    if (i[1] == small):
        lst2.append(i[0])
lst2.sort()

for i in lst2:
    print i
    
  # lists are nested  
