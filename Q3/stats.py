
import math

# in this file, t = , n =  sample size, x_bar = mean, standard deviation = s
# each program will have their own 
def free_degree(n):
    nl = n-1
    nl = round(nl,-1)
    print(f'The degree of freedom is closest to: {nl}')

def moe(t,s,n):
    v = t*(s/math.sqrt(n))
    return v


def mu(mean, v):
    low = mean-v
    higher = mean + v
    print(low)
    print(higher)

n = 52
mean = 53.4
s = 9.4
v = moe(t = 1.676, s = s, n = n)
mu(mean,v)