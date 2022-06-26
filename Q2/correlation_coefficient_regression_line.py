

import math


def correlation_coefficient_and_equation(x, y):
    """This function finds the correleation coeficient and regression line through input lists"""
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
    b1 = r*(sy/sx)
    b0 = mean_y - (b1*mean_x)
    print(f'The correleation coefficient is: r = {r}\n')
    print(f'The regression line equation is: {round(b0,5)} + {round(b1,5)}x')

def opposite_regression_equation(mean_x, mean_y, sx, sy, r):
    """When given the variables, this will output the regression line equation"""
    b1 = r*(sy/sx)
    b0 = mean_y - (b1*mean_x)
    print(f'The regression line equation is: {round(b0,5)} + {round(b1,5)}x')