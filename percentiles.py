import math


def percentile(thislist, p):
    
    L = (p/100)*len(thislist)
    if L % 1 == 0:
        thislist = sorted(thislist)
        L2 = int(L)
        num = L2- 1
        num1 = thislist[num]
        num2 = thislist[L2]
        per = (num1 + num2) / 2
    else:
        thislist = sorted(thislist)
        L2 = math.ceil(L)
        num = L2 - 1
        per = thislist[num]
    print(f'The {p} percentile is: {per}')

    
mylist = [48,27,12,59,16,37,20,42,44,24,27,11,29,14,18,39,21,22,45,8,49,54,30,33]
p = 75
percentile(mylist, p)
