

import math



def sample_mean_difference(x,y,n):
    
    meanlist = []
    sdlist = []
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
    print(f'The mean of difference is: {mean_of_difference}')
    print(f'The standard deviaion of difference is: {standard_deviation_of_difference}')
    test_statistic = mean_of_difference/(standard_deviation_of_difference/math.sqrt(n))
    print(f'test statistic, t = {test_statistic}')