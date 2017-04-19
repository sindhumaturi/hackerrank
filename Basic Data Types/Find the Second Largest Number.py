if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
        
    lst = []
    for i in arr:
        if i not in lst:
            lst.append(i)
    lst.sort()
    print lst[len(lst)-2]
    
    """lst1 = [i for i in arr if i not in lst1].sort()
    print lst[len(lst1)-2]"""
    
    
            
    
            
    
    
