import random
import math

data = []

for i in range(1000):
    data.append(random.randint(0, 100))



mean = sum(data) / len(data)

data.sort()

n = len(data)

if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]

variance = 0

for x in data:
    variance += (x - mean) ** 2

variance = variance / len(data)

std_dev = math.sqrt(variance)



print("Mean =", mean)
print("Median =", median)
print("Standard Deviation =", std_dev)