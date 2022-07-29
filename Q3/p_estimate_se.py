

import math
from lists import z_dict

def point_estimate_standard_error(x,n,percentage):

    p_hat = x/n
    print(f'The point estimate is: {p_hat}')
    num = p_hat*(1-p_hat)
    denom = n
    se = math.sqrt(num/denom)
    print(f'Standard error is: {se}\n')

    for i,j in z_dict.items():
        if percentage == i:
            z = j
            sol = z*se
            print(f'The margin of error is: {sol}\n')
            low_interval = p_hat-sol
            high_interval = p_hat+sol
            print(f'The low end interval is: {low_interval}')
            print(f'The high end interval is: {high_interval}')
        else:
            pass


def margin_of_error(perc):
    # in the 
    global se
    global p_hat

    for i,j in z_dict.items():
        if perc == i:
            z = j
    sol = z*se
    print(f'The margin of error is: {sol}\n')
    low_interval = p_hat-sol
    high_interval = p_hat+sol
    print(f'The low end interval is: {low_interval}')
    print(f'The high end interval is: {high_interval}')

def confidence_interval(xbar,n,sigma, perc):
    for i,j in z_dict.items():
        if perc == i:
            z = j
    zalpha = z
    margin_of_error = (z*sigma)/math.sqrt(n)
    margin_of_error = round(margin_of_error,5)
    left = xbar - (zalpha*(sigma/math.sqrt(n)))
    right = xbar + (zalpha*(sigma/math.sqrt(n)))
    print(f'The margin of error is: {margin_of_error}')
    print(f'The low end interval is: {left}')
    print(f'The high end interval is: {right}')
    print(f'\nAll three data points rounded to the nearest decimal points are as follows:')
    print(f'margin of error = {round(margin_of_error,2)}\nlow end = {round(left,2)}\nhigh end = {round(right,2)}')

