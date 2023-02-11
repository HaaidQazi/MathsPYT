import scipy.stats as stats
import math

mean = 14.18
std = math.sqrt(0.7396)

z1 = 0.583 / std
z2 = 0.405 / std

p1 = stats.norm.cdf(z1, loc=mean, scale=std)
p2 = stats.norm.cdf(z2, loc=mean, scale=std)

prob = p2 - p1

print("The probability of another randomly selected 15-year old student having the same sprint time range is:", prob)
