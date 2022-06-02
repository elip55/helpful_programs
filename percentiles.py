import math


def percentile(thislist, p):
    
    sorted(thislist)
    L = (p/100)*len(thislist)
    if type(L) == int:
        num = L - 1
        num1 = thislist[num]
        num2 = thislist[L]
        per = (num1 + num2) / 2
    if type(L) == float:
        L2 = math.ceil(L)
        num = L2 - 1
        per = thislist[num]
    print(f'The {p} percentile is: {per}')

    
mylist = [2,2,5,5,7,7,8,10,12,12,13,13,14,
         15,15,16,18,18,21,21,22,23,24,24,24,25,
         26,27,28,28,31,32,34,35,35,36,37,37,41,
         43,43,46,47,47,49,50,50,51,52,52,54,55,
         56,58,58,58,59,59,62,64,65,66,70,71,72]
p = 66
percentile(mylist, p)