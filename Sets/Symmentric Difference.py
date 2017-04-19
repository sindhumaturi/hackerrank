input()
n = set(map(int, raw_input().split()))
input()
m = set(map(int, raw_input().split()))    
       
myset = sorted(set(n.union(m).difference(n.intersection(m))))
for i in myset:
        print i