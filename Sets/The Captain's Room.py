n = input()
a = map(int,raw_input().split())
b = set(a)

print (n*sum(b)-sum(a))/(n-1)