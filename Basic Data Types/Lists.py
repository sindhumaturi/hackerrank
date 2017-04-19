if __name__ == '__main__':
    N = int(raw_input())
    lst = []
    for a in range(N):
        ins = raw_input().split()
        if (ins[0] == "insert"):
            i = int(ins[1])
            e = int(ins[2])
            lst.insert(i,e)
        elif (ins[0] == "print"):
            print (lst)
        elif (ins[0] == "remove"):
            r = int(ins[1])
            lst.remove(r)
        elif (ins[0] == "append"):
            app = int(ins[1])
            lst.append(app)
        elif (ins[0] == "sort"):
            lst.sort()
        elif (ins[0] == "pop"):
            if (len(lst) > 1):
                lst.pop()
        elif (ins[0] == "reverse"):
            lst = lst[::-1]
        else:
            pass
            
