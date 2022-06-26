


def p_AorB(a,b, ab):
    # calculates P(A or B)
    P = a + b - ab
    P_C = 1 - a
    print(f'P(A or B) = {P}')
    print(f'P(A^C) = {P_C}')

def basic_probability(a,b):
    # this function calculates basic probabilty
    c = a/b
    print(c)

a = .38
b = .2
ab = .01

p_AorB(a,b,ab)
