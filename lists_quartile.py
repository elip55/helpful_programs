import math


import math


def values(mylist):
    
    sorted(mylist)
    L1 = int((25/100)*len(mylist))
    L3 = int((75/100)*len(mylist))
    num1 = mylist[L1-1]
    num2 = mylist[L1]
    num3 = mylist[L3-1]
    num4 = mylist[L3]
    q1 = (num1 + num2) / 2
    q3 = (num3 + num4) / 2
    print(f'First quartile: {q1}')
    print(f'Third quartile: {q3}')
    iqr = q3 - q1
    lower_outlier = q1 - (1.5)*iqr
    upper_outlier = q3 + (1.5)*iqr
    print(f'The IQR is: {iqr}')
    print(f'The Lower Outlier Boundary is: {lower_outlier}')
    print(f'The Upper Outlier Boundary is: {upper_outlier}')
    
    
mylist = [25,26,26,26,27,28,28,32,34,34,
         35,36,36,36,37,38,40,43,44,47,
         47,48,49,51,51,52,53,54,54,55,
         57,60,61,65,74,76,78,81,82,84]
values(mylist)