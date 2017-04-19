from itertools import combinations
n,r = raw_input().split()
for j in range(1,int(r)+1):
    for i in combinations(sorted(n),j):
        print ''.join(list(i))
