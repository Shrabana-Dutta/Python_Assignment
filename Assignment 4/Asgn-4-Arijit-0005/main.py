# Base class
class Employee:
    def __init__(self, name, years_of_service):
        self.name = name
        self.years_of_service = years_of_service

    def salary(self):
        return 1500 + 100 * self.years_of_service


# Subclass
class Manager(Employee):
    def salary(self):
        return 2500 + 120 * self.years_of_service


# Dictionary-based database
samples = {
    "Rahul": Employee("Rahul", 3),
    "Bikash": Employee("Bikash", 1),
    "Rajan": Manager("Rajan", 10),
    "Priya": Manager("Priya", 3)
}


# Task 1: Create table of employee names and salaries
result = []

for name, obj in samples.items():
    result.append([name, obj.salary()])

print("Employee Salary Table:")
print(result)


# Task 2: Compute average salary
total_salary = 0

for obj in samples.values():
    total_salary += obj.salary()

average_salary = total_salary / len(samples)

print("\nAverage Salary:")
print(average_salary)