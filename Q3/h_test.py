


from cgi import test
from cmath import phase
from lib2to3.pgen2.literals import simple_escapes
import math
from os import P_ALL
from lists import left,right, two_tail

"""NOTE:  You will have to refer back to 'area_graphs' in Q2 to find p value"""

def calc_from_p(h0,n,p):
    nom1 = p-h0
    nom2 = h0*(1-h0)
    denom = math.sqrt(nom2/n)
    z = nom1/denom
    print(f'z = {z}')

def htest(h0,h1,n,x,sigma, alpha1, alpha2):

    xbar = sigma/math.sqrt(n)
    nom = x - h0
    z = nom/xbar
    if h0 != h1:
        two_tailed(h0,h1,n,x,sigma,alpha1,alpha2)
        quit()
    print(f'z = {z}')
    if z > 0:
        for i,j in right.items():
            if i == alpha1:
                cp1 = j
                print(f'The critical value for {alpha1} is: {j}')
            if i == alpha2:
                print(f'The critical value for {alpha2} is: {j}')
                cp2 = j
    
    if z < 0:
        for i,j in left.items():
            if i == alpha1:
                print(f'The critical value for {alpha1} is: {j}')
                cp1 = j
            if i == alpha2:
                print(f'The critical value for {alpha2} is: {j}')
                cp2 = j

def sample_proportion(x,n):
    # use this function to return the p_hat value, this can be used with calc from p
    phat = x/n
    return phat

def test_statistic(x1,x2,mu1,mu2,s1,s2,n1,n2):
    nom = (x1-x2)-(mu1-mu2)
    insquare = (s1**2/n1)+(s2**2/n2)
    denom = math.sqrt(insquare)
    t = nom/denom
    print(f't = {t}')

def two_tailed(h0,n,x,sigma,alpha1,alpha2):
    xbar = sigma/math.sqrt(n)
    nom = x - h0
    z = nom/xbar
    print(f'z = {z}')
    for i,j in two_tail.items():
        if i == alpha1:
            print(f'The critical value for {alpha1} is: {-j} and {j}')
            lower = -j
            upper = j
        if i == alpha2:
            print(f'The critical value for {alpha2} is: {-j} and {j}')
            lower2 = -j
            upper2 = j
    if z <= lower or z>= upper:
        print(f'The hypothesis at {alpha1} is rejected')
    else:
        print(f"The hypothesis at {alpha1} is accepted")
    if z <= lower2 or z>= upper2:
        print(f'The hypothesis at {alpha2} is rejected')
    else:
        print(f"The hypothesis at {alpha2} is accepted")

    

# for this program, if h1 > h0  or h1 < h0, NOTE: make h1 = h0
# the program will compute the rest
x1 = 3.7
s1 = 5.67
x2 = 2.1
s2 = 4.71
n1 = 61
n2 = 63
m1 =1
m2=1
test_statistic(x1,x2,m1,m2,s1,s2,n1,n2)

