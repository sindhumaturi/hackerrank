from itertools import groupby
for key, group in groupby(raw_input()):
    print (len(list(group)),int(key)),