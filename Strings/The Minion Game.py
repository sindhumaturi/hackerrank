def minion_game(string):
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        #for j in range(i+1,len(string)+1):
        if string[i] in ['A','E','I','O','U']:
            kevin += len(string)-i   
        else:
            stuart += len(string)-i  

    if (kevin > stuart):
        print "Kevin", kevin
    elif (kevin < stuart):
        print "Stuart", stuart
    else:
        print "Draw"