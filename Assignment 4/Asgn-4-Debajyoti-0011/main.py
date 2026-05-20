class Employee:

    def __init__(self, name, years):
        self.name = name
        self.years = years

    def salary(self):
        return 1500 + 100 * self.years


class Manager(Employee):

    def salary(self):
        return 2500 + 120 * self.years

database = {
    "Rahul": Employee("Rahul", 3),
    "Bikash": Employee("Bikash", 1),
    "Rajan": Manager("Rajan", 10),
    "Priya": Manager("Priya", 3)
}

table = []

total_salary = 0

for name, obj in database.items():

    sal = obj.salary()

    table.append([name, sal])

    total_salary += sal

average_salary = total_salary / len(database)


print("Table:")
print(table)

print("Average Salary:", average_salary)
