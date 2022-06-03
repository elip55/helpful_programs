import math

    
# z-score
# mu = mean score
# sigma = standard deviation

def z_score(x,mu,sigma):
    z = (x-mu)/sigma
    print(round(z,2))

def z_score_opposite(z,mu,sigma):
    x = z*sigma + mu
    print(round(x,2))

    
z = -.6
m = 170
s = 30
z_score_opposite(z,m,s)