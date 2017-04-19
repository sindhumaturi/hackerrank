import itertools
n = input()
N = map(str,raw_input().split())
k = input()
p = 0      
lst1 = list(itertools.combinations(N,k))
for i in lst1:
    if 'a' in i:
        p += 1
print "%.3f" %(float(p)/len(lst1))
