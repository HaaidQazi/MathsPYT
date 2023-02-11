import math

def poisson_probability(lambda_value, k):
    return (lambda_value**k * math.exp(-lambda_value)) / math.factorial(k)

lambda_value = 2 # 2 taxis per minute

# a) Find the probability of exactly 2 taxis arriving during a particular minute.
prob_2_taxis = poisson_probability(lambda_value, 2)
print(f"Probability of exactly 2 taxis arriving during a particular minute: {prob_2_taxis}")

# b) Find the probability of at most 1 taxi arriving during a particular minute.
prob_1_taxi_or_less = poisson_probability(lambda_value, 0) + poisson_probability(lambda_value, 1)
print(f"Probability of at most 1 taxi arriving during a particular minute: {prob_1_taxi_or_less}")

# c) Find the probability of the time between two consecutive taxi arrivals being at most 1 minute.
prob_time_between_taxis_1_minute_or_less = 1 - math.exp(-lambda_value)
print(f"Probability of the time between two consecutive taxi arrivals being at most 1 minute: {prob_time_between_taxis_1_minute_or_less}")

# Output:
# Probability of exactly 2 taxis arriving during a particular minute: 0.2706705664732254
# Probability of at most 1 taxi arriving during a particular minute: 0.6766764161830635
# Probability of the time between two consecutive taxi arrivals being at most 1 minute: 0.8646647167633873
