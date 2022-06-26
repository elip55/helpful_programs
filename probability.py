
from cmath import sqrt
import math

def p(n,p,x):
    
    v = n-x
    p1 = math.factorial(n) / (math.factorial(x)*math.factorial(v))
    p2 = p**x
    p3 = (1-p)**(n-x)
    P = p1*p2*p3
    mu_x = round(n*p,2)
    variance = (n*p)*(1-p)
    standard_devation = math.sqrt(variance)
    print(f'The probability is: {P}')
    print(f'The mean is: {mu_x}')
    print(f'The variance is: {variance}')
    print(f'The standard deviation is: {standard_devation}')


def p_lower(n,p,x):

    sum_list = []
    for i in range(x+1):
        v = n-i
        p1 = math.factorial(n) / (math.factorial(i)*math.factorial(v))
        p2 = p**i
        p3 = (1-p)**(n-i)
        P = p1*p2*p3
        sum_list.append(P)
    sol = sum(sum_list)
    print(f'The probability of {x} or lower is: {sol}')

def p_higher(n,p,x):
    # be mindful of the question
    # since i add +1 to x, be cautious of initial value
    c = x
    sum_list = []
    for i in range(n-x):
        x +=1
        v = n-x
        p1 = math.factorial(n) / (math.factorial(x)*math.factorial(v))
        p2 = p**x
        p3 = (1-p)**(n-x)
        P = p1*p2*p3
        sum_list.append(P)

    sol = sum(sum_list)
    print(f'The probability of {c} or higher is: {sol}')

