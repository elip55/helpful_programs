


import math

def perc(mu,z,sigma):
    x = mu + z*sigma
    print(x)


def prop(mu,x,sigma):
    z = (x-mu)/sigma
    print(z)


def standard_dev_and_perc(sigma,n,x_bar,mu):
    
    standard_deviation = sigma/math.sqrt(n)
    z = (x_bar-mu)/standard_deviation
    print(f'The Standard Deviation is: {standard_deviation}')
    print(f'Z = {z}')
