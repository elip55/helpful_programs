


import math

def percentile(mu,z,sigma):
    x = mu + z*sigma
    print(f'The percentile is: {x}')


def prop(mu,x,sigma):
    z = (x-mu)/sigma
    print(z)

def sd(sigma,n,x,mu):
    
    sigma_x = sigma/math.sqrt(n)
    z_bar = (x-mu)/sigma_x
    z_score = (x-mu)/sigma
    sigma = round(sigma,5)
    z_bar = round(z_bar,5)
    print(f'Standard deviation = {sigma_x}')
    print(f'z = {z_bar}')
    print(f'from z score, z = {z_score}')
