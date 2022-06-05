


import math

# this file computes mean, sample variance, standard deviation, and correlation coeficient

def calc(numbers):
    """This function finds mean, sample variance, and standard deviation through input lists"""
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


def correlation_coeficient(x, y):
    """This function finds the correleation coeficient through input lists"""
    denom = len(x) # this shouldn't matter as all lists should be equal
    mean_x = sum(x)/len(x)
    lx1 = []
    lx2 = []
    for i in x:
        x1 = (i - mean_x)**2
        x1 = abs(x1)
        lx1.append(x1)
        x2 = i - mean_x
        lx2.append(x2)
    sum_x_squared = sum(lx1)
    ly1 = []
    ly2 = []
    mean_y = sum(y)/len(y)
    for i in y:
        y1 = (i - mean_y)**2
        y1 = abs(y1)
        ly1.append(y1)
        y2 = i - mean_y
        ly2.append(y2)
    sum_y_squared = sum(ly1)
    sx = math.sqrt(sum_x_squared/(denom - 1))
    sy = math.sqrt(sum_y_squared/(denom - 1))
    
    final_sum_list = []
    for i,j in zip(lx2,ly2):
        x_over_s = i/sx
        y_over_s = j/sy
        sum_values = x_over_s*y_over_s
        final_sum_list.append(sum_values)
    final_sum = sum(final_sum_list)
    r = final_sum/(denom-1)
    print(f'The correleation coefficient is: {r}')
    
    
x = [
247,
124,
95,
18,
2]

y = [
232,
146,
128,
23,
2]

correlation_coeficient(x, y)


