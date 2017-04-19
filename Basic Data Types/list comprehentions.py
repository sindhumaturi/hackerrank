if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    lst = []
    for i in range (x+1):
        for j in range (y+1):
            for k in range (z+1):
                if (i+j+k != n):
                    lst1 = []
                    lst1.append(i)
                    lst1.append(j)
                    lst1.append(k)
                    lst.append(lst1)
    print lst
    
    #print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
                   
                    
                    
                    
