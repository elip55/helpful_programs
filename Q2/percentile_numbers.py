import math

# This is a file where you can find specific number percentiles

def percentile_from_list(thislist, p):
    # this function is for a specific percentile percentage ex: quarter and above
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

def percentile_from_num(thislist, p):
    # this function is for a specific percentile
    thislist = sorted(thislist)
    newlist = []
    for i in thislist:
        if i < p:
            newlist.append(i)
        
    percentile = 100*((len(newlist)+.5)/len(thislist))
    print(f'The percentile is: {percentile}')

# place values here
