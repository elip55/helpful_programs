
import math

# this only works with whole numbers

def values(mylist):
    
    mylist = sorted(mylist)
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
    
    
sea = [.6,1.3,2.5,1.5,1.1,1.1,2.2,.6,1.5,1.5,1.2,1.6,2.1,6.6,4,2.5,1.4,1.4,1.8,1.6,3.7,.6,2.7,2.6,3,1.2,1,1.6,3.1,2.4]
high = [4.7,1.9,9.1,837,9.5,2.7,9.2,7.3,2.1,6.3,6.5,6.3,2,5.9,5.6,5.6,1.5,6.5,5.3,5.6,2.1,1.1,3.3,1.8,7.6,8.9,4.4,3.6,4.4,3.8]
