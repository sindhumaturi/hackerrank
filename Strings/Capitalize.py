def capitalize(string):
    s = ""
    for i in range(len(string)):
        if (string[i] != " "):
            if (i == 0 or (i!= 0 and string[i-1] == " ")):
                s = s + string[i].upper()
            else:
                s = s + string[i]
        else:
            s = s + " "
    return s
    #capitalizes the string
