

import math
from z_list_from_tdistribution import z_dict

def point_estimate_standard_error(x,n):
    global se
    global p_hat

    p_hat = x/n
    print(f'The point estimate is: {p_hat}')
    num = p_hat*(1-p_hat)
    denom = n
    se = math.sqrt(num/denom)
    print(f'Standard error is: {se}\n')

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

x = 50
n = 119
perc = 80
point_estimate_standard_error(x,n)
margin_of_error(perc)




