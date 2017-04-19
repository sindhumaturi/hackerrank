# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
N = set(map(int, raw_input().split()))
b = input()
B = set(map(int, raw_input().split()))

print len(N.difference(B))