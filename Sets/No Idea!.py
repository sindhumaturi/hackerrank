# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, raw_input().split())
array = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        happiness += 0
print happiness

#print len(set(array).intersection(A))- len(set(array).intersection(B))