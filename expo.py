import math

def exponential_distribution(x, lam):
    return lam * math.exp(-lam * x)

def cumulative_distribution(x, lam):
     return 1 - math.exp(-lam * x)
lam = 0.1
x=7
prob = cumulative_distribution(x, lam)
prob = 1 - prob
print("The probability that a computer part lasts more than 7 years:", prob)


