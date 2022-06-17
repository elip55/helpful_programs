



import math

def mean_mu_zip(x,y):
    # from two lists, this will find mean, mu_x, and standard deviation
    zip_list = []
    sd_list = []
    for i,j in zip(x,y):
        mu_x_list = i*j
        zip_list.append(mu_x_list)
    mu_x = sum(zip_list)
    for i,j in zip(x,y):
        v2 = i - mu_x
        v_2 = v2**2
        v3 = v_2*j
        sd_list.append(v3)
    variance = sum(sd_list)
    standard_deviation = math.sqrt(variance)
    print(f'MUx is: {mu_x}')
    print(f'Variance is: {variance}')
    print(f'Standiard Deviation is: {standard_deviation}')

def find_one(x):
    # if you have a missing probabilty number in the distribution, use this function to find it
    v = sum(x)
    sol = 1 - v
    sol = round(sol, 2)
    print(f'The missing number is : {sol}')

