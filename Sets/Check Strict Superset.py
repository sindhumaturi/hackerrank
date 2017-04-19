A = set(map(int, raw_input().split()))
n = input()
x = 0
for i in range(n):
    B = set(map(int, raw_input().split()))
    if (B.difference(A) == set()):
        x += 1
if (n == x):
    print "True"
else:
    print "False"