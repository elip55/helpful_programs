import math
from zlib import Z_NO_COMPRESSION

    
# z-score
# mu = mean score
# sigma = standard deviation

def z_score(x,mu,sigma):
    # when provided with the test score itself
    z = (x-mu)/sigma
    print(round(z,2))

def z_score_opposite(z,mu,sigma):
    # when provided with the z-score first
    x = z*sigma + mu
    print(round(x,2))

    

# place values here
