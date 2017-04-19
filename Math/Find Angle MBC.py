import math
AB = input()
BC = input()
if (AB == BC):
    print "45"+'°'
else:
    #print str(round(math.degrees(math.atan2(AB/BC))))+'°'
    print str(int(round(math.degrees(math.atan2(AB,BC)))))+'°'