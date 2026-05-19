import random
import math

class Stat:
    def __init__(self):
        self.data = [random.randint(1, 100) for i in range(1000)]
    
    def mean(self):
        return sum(self.data)/len(self.data)
    
    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]

    def variance(self):
        Ex2 = sum(list(map(lambda x: x**2, self.data)))/len(self.data)
        Ex_2 = (sum(self.data)/len(self.data))**2
        return Ex2-Ex_2
    
    def std_dev(self):
        return math.sqrt(self.variance())

s = Stat()
print("Mean: ", s.mean())
print("Median: ", s.median())
print("Variance: ", s.variance())
print("Standard Deviation: ", s.std_dev())