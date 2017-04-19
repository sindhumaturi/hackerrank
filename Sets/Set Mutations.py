# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
A = set(map(int,raw_input().split()))
for i in range(input()):
    op = raw_input().split()
    if (op[0] == "intersection_update"):
        s = set(map(int,raw_input().split()))
        A.intersection_update(s)
    elif (op[0] == "update"):
        s = set(map(int,raw_input().split()))
        A.update(s)
    elif (op[0] == "symmetric_difference_update"):
        s = set(map(int,raw_input().split()))
        A.symmetric_difference_update(s)
    elif (op[0] == "difference_update"):
        s = set(map(int,raw_input().split()))
        A.difference_update(s)
    else:
        pass
     
print sum(A)
    
        