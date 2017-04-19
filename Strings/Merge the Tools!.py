def merge_the_tools(string, k):
    n = len(string)
    lst = []
    for i in range(0,n,k):
        lst.append(string[i:i+k])

    for j in range(n/k):
        s = ''
        for p in range(k):
            if lst[j][p] not in s:
                s = s+lst[j][p] 
        print s