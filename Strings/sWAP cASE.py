def swap_case(s):
    str = ''
    for i in s:
        if (i.islower()):
            str = str + i.upper()
        elif (i.isupper()):
            str = str + i.lower()
        else:
            str = str + i
    return str
