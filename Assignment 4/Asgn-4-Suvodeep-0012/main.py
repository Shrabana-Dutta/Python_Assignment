# Base class
class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = years_of_service

    # Salary method
    def salary(self):
        return 1500 + (100 * self.years_of_service)


# Subclass
class Manager(Employee):

    # Overriding salary method
    def salary(self):
        return 2500 + (120 * self.years_of_service)


# Dictionary database
samples = {
    "Rahul": Employee("Rahul", 3),
    "Bikash": Employee("Bikash", 1),
    "Rajan": Manager("Rajan", 10),
    "Priya": Manager("Priya", 3)
}

# Creating table
result = []

total_salary = 0

for name, obj in samples.items():
    sal = obj.salary()
    result.append([name, sal])
    total_salary += sal

# Display table
print("Employee Salary Table:")
print(result)

# Average salary
average_salary = total_salary / len(samples)

print("Average Salary =", average_salary)