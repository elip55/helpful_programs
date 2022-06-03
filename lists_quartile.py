import math
import statistics

# so far this only works with whole numbers

def values(mylist):
    
    mylist = sorted(mylist)
    med =  statistics.median(mylist)
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
    print(f'The median is: {med}')
    print(f'The IQR is: {iqr}')
    print(f'The Lower Outlier Boundary is: {lower_outlier}')
    print(f'The Upper Outlier Boundary is: {upper_outlier}')

# place values here