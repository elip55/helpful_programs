import math

from lists import left,right, two_tail, z_dict
from h_test import two_tailed, htest, htest_P, test_statistict_two_samples_simplified, test_statistic_z, test_statistict_tlist
from p_estimate_se import point_estimate_standard_error, confidence_interval

"""NOTE:  this is to simplify the final for stats"""

def confidence_interval_initiate(xbar,n,sigma, perc):
    confidence_interval(xbar,n,sigma,perc)




def point_estimate_initiate(x,n,percentage):
    point_estimate_standard_error(x,n,percentage)



def htest_initiate_mu(h0,h1,n,x,sigma,alpha1,alpha2):
    # NOTE:  input h0!=h1 manually to initiate the correct porgrams
    if h0 != h1:
        two_tailed(h0,h1,n,x,sigma,alpha1,alpha2)
        quit()
    else:
        htest(h0,h1,n,x,sigma,alpha1,alpha2)



def htest_initiate_P(n,x,p,alpha1,alpha2):
    htest_P(n,x,p,alpha1,alpha2)


def rejection(p,alpha):
    if p<=alpha:
        print(f'We reject\nThere IS enough evidence to conclude.')
    else:
        print(f'We do not reject\nThere is NOT enough evidence to conclude.')


def t_stat_two_sample_simple_initiate(mu1,mu2,s1,s2,n1,n2):
    test_statistict_two_samples_simplified(mu1,mu2,s1,s2,n1,n2)


def t_stat_no_mean_initiate(x1,x2,n1,n2):
    test_statistic_z(x1,x2,n1,n2)

def tlist_initiate(a,b,mu1):
    test_statistict_tlist(a,b,mu1)

print('REMEMBER IF ITS DOUBLE TAILED, ALPHA MUST BE DEVIDED BY 2!\n')


