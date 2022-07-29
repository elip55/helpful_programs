


from hashlib import pbkdf2_hmac
import math

from lists import left,right, two_tail

"""NOTE:  You will have to refer back to 'area_graphs' in Q2 to find p value"""

def htest_P(n,x,p,alpha1,alpha2):
    p_hat = x/n
    num = p_hat - p
    num2 = p*(1-p)
    denom2 = n
    denom = math.sqrt(num2/denom2)
    z = num/denom
    if z > 0:
        for i,j in right.items():
            if i == alpha1:
                cp1 = j
                print(f'The critical value for {alpha1} is: {j}')
            if i == alpha2:
                print(f'The critical value for {alpha2} is: {j}')
                cp2 = j
    print('REMEMBER: P value is found with area graphs!')
    
    if z < 0:
        for i,j in left.items():
            if i == alpha1:
                print(f'The critical value for {alpha1} is: {j}')
                cp1 = j
            if i == alpha2:
                print(f'The critical value for {alpha2} is: {j}')
    print(f'z = {z}')

def htest(h0,h1,n,x,sigma, alpha1, alpha2):

    xbar = sigma/math.sqrt(n)
    nom = x - h0
    z = nom/xbar
    print(f'z = {z}')
    if z > 0:
        for i,j in right.items():
            if i == alpha1:
                cp1 = j
                print(f'The critical value for {alpha1} is: {j}')
            if i == alpha2:
                print(f'The critical value for {alpha2} is: {j}')
                cp2 = j
    print('REMEMBER: P value is found with area graphs!')
    
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

def test_statistict_two_samples_simplified(mu1,mu2,s1,s2,n1,n2):
    nom = mu1 - mu2
    insquare = (s1**2/n1)+(s2**2/n2)
    denom = math.sqrt(insquare)
    t = nom/denom
    if n1 < n2:
        degrees_of_freedom = n1-1
    else:
        degrees_of_freedom = n2-1
    print(f't = {t}')
    print(f'Degrees of freedom are: {degrees_of_freedom}')

def test_statistict_two_samples(x1,x2,mu1,mu2,s1,s2,n1,n2):
    nom = (x1-x2)-(mu1-mu2)
    insquare = (s1**2/n1)+(s2**2/n2)
    denom = math.sqrt(insquare)
    t = nom/denom
    if n1 < n2:
        degrees_of_freedom = n1-1
    else:
        degrees_of_freedom = n2-1
    print(f't = {t}')
    print(f'Degrees of freedom are: {degrees_of_freedom}')

def test_statistict_tlist(a,b,mu1,mu2):
    n1 = len(a)
    n2 = len(b)
    x1 = sum(a)/len(a)
    x2 = sum(b)/len(b)
    s1list = []
    s2list = []
    for i,j in zip(a,b):
        val1 = abs(i-x1)
        val1 = val1**2
        s1list.append(val1)
        val2 = abs(j-x2)
        val2 = val2**2
        s2list.append(val2)
    sv1 = sum(s1list)/(len(s1list)-1)
    sv2 = sum(s2list)/(len(s2list)-1)
    s1 = math.sqrt(sv1)
    s2 = math.sqrt(sv2)
    nom = (x1-x2)-(mu1-mu2)
    insquare = (s1**2/n1)+(s2**2/n2)
    denom = math.sqrt(insquare)
    t = nom/denom
    if n1 < n2:
        degrees_of_freedom = n1-1
    else:
        degrees_of_freedom = n2-1
    print(f't = {t}')
    print(f'Degrees of freedom are: {degrees_of_freedom}')

def test_statistic_z(x1,x2,n1,n2):
    p1 = x1/n1
    p2 = x2/n2
    p_bar = (x1+x2)/(n1+n2)
    num = p1-p2
    denom = math.sqrt(((p_bar*(1-p_bar))/n1)+(p_bar*(1-p_bar)/n2))
    z = num/denom
    print(f'z = {z}')

def two_tailed(h0,h1,n,x,sigma,alpha1,alpha2):
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
        else: # added this in case there is no alpha2
            exit()
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