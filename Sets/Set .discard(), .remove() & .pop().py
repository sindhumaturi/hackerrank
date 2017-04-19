n = input()
s = set(map(int, raw_input().split())) 
for i in range(input()):
    a = raw_input().split()
    if (a[0] == "pop"):
        if (s != set()):
            s.pop()
    elif (a[0] == "remove"):
        if int(a[1]) in s:
            s.remove(int(a[1]))
    elif (a[0] == "discard"):
        s.discard(int(a[1]))
    else:
        pass
print sum(s)
        
