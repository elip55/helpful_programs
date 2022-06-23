
from all_lists import z_column, zero_column, one_column, two_column, three_column, four_column, five_column, six_column, seven_column, eight_column, nine_column

from all_lists import z2, negOne, negTwo, negThree, negFour, negFive, negSix, negSeven, negEight, negNine
    
    
"""NOTE:  VERY IMPORTANT!!!!!!!  calc_n refers to the hundredths place columns. 
    So, calc_zeros = .00, calc_ones = .01,  calc_twos = .02, and so on.  
    So, simply input the number UP TO the hundredths place number, call the function of the hundredthc place column, and it will return your value."""


def area_calc_zeros(x):
    
    global z_column
    global zero_column
    
    zero_dict = dict(zip(z_column,zero_column))
    for i,j in zero_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_ones(x):
    
    global z_column
    global one_column
    
    one_dict = dict(zip(z_column,one_column))
    for i,j in one_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_twos(x):
    
    global z_column
    global two_column
    
    two_dict = dict(zip(z_column,two_column))
    for i,j in two_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_threes(x):
    
    global z_column
    global three_column
    
    three_dict = dict(zip(z_column,three_column))
    for i,j in three_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_fours(x):
    
    global z_column
    global four_column
    
    four_dict = dict(zip(z_column,four_column))
    for i,j in four_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v


def area_calc_fives(x):
    
    global z_column
    global five_column
    
    five_dict = dict(zip(z_column,five_column))
    for i,j in five_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v


def area_calc_sixes(x):
    
    global z_column
    global six_column
    
    six_dict = dict(zip(z_column,six_column))
    for i,j in six_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_sevens(x):
    
    global z_column
    global seven_column
    
    seven_dict = dict(zip(z_column,seven_column))
    for i,j in seven_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_eights(x):
    
    global z_column
    global eight_column
    
    eight_dict = dict(zip(z_column,eight_column))
    for i,j in eight_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def area_calc_nines(x):
    
    global z_column
    global nine_column
    
    nine_dict = dict(zip(z_column,nine_column))
    for i,j in nine_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a0(x):
    
    global z2
    global negZero
    
    zero_dict = dict(zip(z2,negZero))
    for i,j in zero_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a1(x):
    
    global z2
    global negOne
    
    one_dict = dict(zip(z2,negOne))
    for i,j in one_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a2(x):
    
    global z2
    global negTwo
    
    two_dict = dict(zip(z2,negTwo))
    for i,j in two_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a3(x):
    
    global z2
    global negThree

    
    three_dict = dict(zip(z2,negThree))
    for i,j in three_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a4(x):
    
    global z2
    global negFour
    
    four_dict = dict(zip(z2,negFour))
    for i,j in four_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v


def neg_a5(x):
    
    global z2
    global negFive
    
    five_dict = dict(zip(z2,negFive))
    for i,j in five_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

"""NOTE:  here stars negatives"""
def neg_a6(x):
    
    global z2
    global negSix
    
    six_dict = dict(zip(z2,negSix))
    for i,j in six_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a7(x):
    
    global z2
    global negSeven
    
    seven_dict = dict(zip(z2,negSeven))
    for i,j in seven_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a8(x):
    
    global z2
    global negEight
    
    eight_dict = dict(zip(z2,negEight))
    for i,j in eight_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v

def neg_a9(x):
    
    global z2
    global negNine
    
    nine_dict = dict(zip(z2,negNine))
    for i,j in nine_dict.items():
        if i == x:
            v = j
        else:
            pass
    v2 = 1-v
    print(f'The area to the left of {x} is: {v}')
    print(f'The area to the right of {x} is: {v2}')
    return v


"""NOTE:  VERY IMPORTANT.  Remember that these functions return values LEFT OF the desired point.
    To find the area right of the desired point, simply subtract the value by 1."""