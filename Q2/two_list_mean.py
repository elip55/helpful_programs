



import math

def mean_mu_zip(x,y):
    # from two lists, this will find mean, µx, and standard deviation ∑x
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
    print(f'µx = {mu_x}')
    print(f'Variance is: {variance}')
    print(f'∑x = {standard_deviation}')

def find_one(x):
    # if you have a missing probabilty number in the distribution, use this function to find it
    v = sum(x)
    sol = 1 - v
    sol = round(sol, 2)
    print(f'The missing number is : {sol}')

v = [0,
1,
2,
3,
4]

w = [0.3,
0.2,
0.2,
0.2,
0.1]

mean_mu_zip(v,w)