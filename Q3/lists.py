
# t list distribution lists
percentage = [20.0, 50.0, 80.0, 90.0, 95.0, 98.0, 99.0, 99.5, 99.8, 99.9]
solution = [0.253,0.674, 1.282, 1.645, 1.960, 2.326, 2.576, 2.807, 3.090, 3.291]
z_dict = dict(zip(percentage,solution))


# Hypothesis tests
h1 = [.1,.05,.02,.01]
negative = [-1.282,-1.645,-2.054,-2.326]
positive = [ -x for x in negative]
plus_or_minus = [1.645,1.96,2.326,2.576]

left = dict(zip(h1, negative))
right = dict(zip(h1, positive))
two_tail = dict(zip(h1, plus_or_minus))