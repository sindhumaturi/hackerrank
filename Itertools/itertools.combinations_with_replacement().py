from itertools import combinations_with_replacement
n,r = raw_input().split()
for i in combinations_with_replacement(sorted(n),int(r)):
    print ''.join(list(i))