from itertools import permutations
n,r = raw_input().split()
for i in sorted(permutations(n,int(r))):
    print ''.join(list(i))