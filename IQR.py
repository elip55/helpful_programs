import math

def iqr(q1, q2, q3):
    
    iqr = q3 - q1
    lower_outlier = q1 - (1.5)*iqr
    upper_outlier = q3 + (1.5)*iqr
    print(f'The IQR is: {iqr}')
    print(f'The Lower Outlier Boundary is: {lower_outlier}')
    print(f'The Upper Outlier Boundary is: {upper_outlier}')

q1 = 105
q2 = 106
q3 = 120
iqr(q1, q2, q3)