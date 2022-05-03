class Employee():

    def __init__(self, first_name, last_name, salary, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

    def change_salary(self, percent_increase):
        
        if percent_increase > 10:
            return None

        new_salary = self.salary * (1 + (.01 * percent_increase))

        if not new_salary < 40000:
            self.salary = new_salary


employee_1 = Employee("Alex", "Smith", 82000)
employee_2 = Employee("Bradley", "Jones", 79000)
employee_3 = Employee("Charlie", "Adams", 65000)
employee_4 = Employee("Darla", "Smith", 85000, middle_name = "Allison")
employee_5 = Employee("Eric", "Smith", 40000)

employees = [employee_1, employee_2, employee_3, employee_4, employee_5]

for employee in employees:
    print(f"Full name: {employee.full_name()}, salary: {employee.salary}")

for employee in employees:
    employee.change_salary(-3)
    # call method to change salary

for employee in employees:
    print(f"Full name: {employee.full_name()}, salary: {employee.salary}")