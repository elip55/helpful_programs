

import math


def mu_d_sample(mod,sdod,mu_d,n):
    degree_freedom = n-1
    test_statistic = (abs(mod) - mu_d)/(sdod/math.sqrt(n))
    print(f'test statistic, t = {test_statistic}')
    print(f'The degree of freedom is: {degree_freedom}')

def sample_mean_difference(x,y,mu_d):
    n = len(x)
    meanlist = []
    sdlist = []
    degree_freedom = n-1
    for i,j in zip(x,y):
        num0 = i-j
        meanlist.append(num0)
    mean_of_difference = sum(meanlist)/len(meanlist)
    for i in meanlist:
        num1 = abs(i - mean_of_difference)
        num2 = num1**2
        sdlist.append(num2)
    sample_variance = sum(sdlist)/(len(sdlist)-1)
    standard_deviation_of_difference = math.sqrt(sample_variance)
    if mu_d != 0:
        mu_d_sample(mean_of_difference,standard_deviation_of_difference,mu_d,n)
    else:
        test_statistic = (mean_of_difference - mu_d)/(standard_deviation_of_difference/math.sqrt(n))
        print(f'test statistic, t = {test_statistic}')
        print(f'The degree of freedom is: {degree_freedom}')


a = [394,
513,
483,
447,
440,
473,
440,
481,
459,
399]
b = [430,
525,
482,
482,
479,
493,
466,
482,
455,
404]

mu_d = 15
sample_mean_difference(a,b,mu_d)