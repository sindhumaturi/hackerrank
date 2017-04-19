def print_rangoli(size):
    width = (size*4)-3
    lst = []
    string1 = ''
    for i in range(size):
        lst.append(chr(97+i))
    if (size > 1):
        for j in range(1,size+1):
            string = ('-'.join(list(string1))+'-'+lst[size-j]+'-'+'-'.join(list(string1[::-1]))).center(width,'-')
            string1 = string1 + lst[size-j]
            print string

        for k in range(1,size):
            string1 = string1[:-1]
            string3 = string1 + string1[:-1][::-1] 
            print ('-'.join(list(string3))).center(width,'-')
    else:
        print chr(97)
    