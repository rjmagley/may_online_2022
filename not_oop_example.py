employees = []

employees.append({"first_name": "Alex", "last_name": "Smith", "salary": 87000})
employees.append({"first_name": "Bradley", "last_name": "Jones", "salary": 62000})
employees.append({"first_name": "Charlie", "last_name": "Adams", "salary": 89000})

# new employee
employees.append({"first_name": "David", "last_name": "Jones", "salary": 73000})

# another new employee
employees.append({"first_name": "Eeeeee", "last_name": "Smith", "salary": 98000})

# another another new employee
employees.append({"first_name": "Francis", "last_name": "Alexander", "salary": 82000})

for employee in employees:
    print(f"First name: {employee['first_name']}, last name: {employee['last_name']}, salary: {employee['salary']}")

print("Increasing salary...")
for employee in employees:
    employee["salary"] = employee["salary"] * 105

print("After increase:")
for employee in employees:
    print(f"First name: {employee['first_name']}, last name: {employee['last_name']}, salary: {employee['salary']}")