


import math
import statistics
# this file computes mean, sample variance, standard deviation, and correlation coeficient

def simple_calc_stats(numbers):
    """This function finds mean, sample variance, and standard deviation through input lists"""
    mean = sum(numbers)/len(numbers)
    l1 = []
    for i in numbers:
        val = abs(i - mean)
        val2 = val**2
        l1.append(val2)
    med =  statistics.median(l1)
    sample_variance = sum(l1)/(len(l1)-1)
    population_variance = sum(l1)/len(l1)
    population_standard_deviation = math.sqrt(population_variance)
    standard_deviation = math.sqrt(sample_variance)
    print(f'mean: {mean}')
    print(f'The median is: {med}\n')
    print(f'The population variance is: {population_variance}')
    print(f'The population standard deviation is: {population_standard_deviation}\n')
    print(f'sample variance: {sample_variance}')
    print(f'standard deviation: {standard_deviation}\n')
