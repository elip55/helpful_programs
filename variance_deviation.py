


import math


def calc(numbers):
    
    mean = sum(numbers)/len(numbers)
    l1 = []
    for i in numbers:
        val = abs(i - mean)
        val2 = val**2
        l1.append(val2) 
    sample_variance = sum(l1)/(len(l1)-1)
    standard_deviation = math.sqrt(sample_variance)
    print(f'mean: {mean}')
    print(f'sample variance: {sample_variance}')
    print(f'standard deviation: {standard_deviation}')
l = 307,276,263,299,252,271,284,358,304,303,319,327 # add any list of numbers here and the program will do the work
calc(l)