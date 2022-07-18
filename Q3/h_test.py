


import math

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

def pooled_proportion(x1,x2,n1,n2):
    phat = (x1+x2)/(n1+n2)
    return phat

def test_statistict_t(x1,x2,mu1,mu2,s1,s2,n1,n2):
    nom = (x1-x2)-(mu1-mu2)
    insquare = (s1**2/n1)+(s2**2/n2)
    denom = math.sqrt(insquare)
    t = nom/denom
    print(f't = {t}')

def test_statistic_z(p0,p1,p2,n1,n2):
    nom = p1-p2 
    para1 = p0*(1-p0)
    para2 = (1/n1)+(1/n2)
    denom = math.sqrt(para1*para2)
    z = nom/denom
    print(f'z = {z}')

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


p = pooled_proportion(45,22,337,88)
p1 = sample_proportion(45,337)
p2 = sample_proportion(22,88)
test_statistic_z(p,p1,p2,337,88)