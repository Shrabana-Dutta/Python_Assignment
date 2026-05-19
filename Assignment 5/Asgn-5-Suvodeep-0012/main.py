import random
import math

data = []

# Generate 1000 random numbers
for i in range(1000):
    num = random.randint(1, 100)
    data.append(num)

# ---------------- MEAN -------------------------
total = 0

for num in data:
    total += num

mean = total / len(data)

# ---------------- MEDIAN ----------------
data.sort()

n = len(data)


median = (data[n//2 - 1] + data[n//2]) / 2



# -------------STANDARD DEVIATION----------------
sum_square = 0

for num in data:
    sum_square += (num - mean) ** 2

variance = sum_square / len(data)

standard_deviation = math.sqrt(variance)


# .....................OUTPUT....................
print("Mean =", mean)
print("Median =", median)
print("Standard Deviation =", standard_deviation)