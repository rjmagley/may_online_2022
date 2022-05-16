from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.department import Department

from flask import flash

import re

class Employee():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.middle_name = data['middle_name']
        self.last_name = data['last_name']
        self.salary = data['salary']
        self.department_id = data['department_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.department = None

    @property
    def full_name(self):
        if self.middle_name != None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    # before we had departments involved:
    # @classmethod
    # def get_all_employees(cls):
    #     query = "SELECT * FROM employees;"

    #     results = connectToMySQL("apr_employees").query_db(query)

    #     print(results)

    #     employees = []

    #     for row in results:
    #         employees.append(Employee(row))

    #     return employees

    @classmethod
    def get_all_employees(cls):
        query = "SELECT * FROM employees JOIN departments ON employees.department_id = departments.id;"

        results = connectToMySQL("apr_employees").query_db(query)

        employees = []

        for row in results:

            new_employee = Employee(row)

            department_data = {
                'id': row['departments.id'],
                'name': row['name'],
                'location': row['location'],
                'created_at': row['departments.created_at'],
                'updated_at': row['departments.updated_at']
            }

            new_department = Department(department_data)

            new_employee.department = new_department

            employees.append(new_employee)

        return employees

    @classmethod
    def create_employee(cls, data):
        query = "INSERT INTO employees (first_name, middle_name, last_name, salary, department_id) VALUES (%(first_name)s, %(middle_name)s, %(last_name)s, %(salary)s, %(department_id)s);"

        result = connectToMySQL("apr_employees").query_db(query, data)

        return result


    @classmethod
    def delete_employee(cls, data):
        query = 'DELETE FROM employees WHERE id = %(employee_id)s;'

        connectToMySQL("apr_employees").query_db(query, data)

    @classmethod
    def get_employee_by_id(cls, data):
        query = 'SELECT * FROM employees WHERE id = %(employee_id)s;'

        results = connectToMySQL("apr_employees").query_db(query, data)

        employee = Employee(results[0])

        return employee

    @classmethod
    def update_employee(cls, data):

        query = "UPDATE employees SET first_name = %(first_name)s, middle_name = %(middle_name)s, last_name = %(last_name)s, salary = %(salary)s WHERE id = %(employee_id)s;"

        result = connectToMySQL("apr_employees").query_db(query, data)

        return result

    # non-regex validation
    # @staticmethod
    # def validate_employee(data):

    #     is_valid = True

    #     # write validation logic here
    #     # must have a first name
    #     # first name 1 to 50 characters in length

    #     if data['first_name'] == '':
    #         is_valid = False
    #         flash("First name should not be empty; first name should be 1 to 50 characters long")
        
    #     elif len(data['first_name']) > 50:
    #         is_valid = False
    #         flash("First name should be 1 to 50 characters long")

    #     # middle name is not needed, but if present
    #     # must also be 1 to 50 characters long

    #     if data['middle_name'] != None:
    #         if len(data['middle_name']) > 50:
    #             is_valid = False
    #             flash("Middle name should be 1 to 50 characters long (or left blank)")

    #     # last name 1 to 50 characters
    #     if data['last_name'] == '':
    #         is_valid = False
    #         flash("Last name should not be empty; first name should be 1 to 50 characters long")
        
    #     elif len(data['last_name']) > 50:
    #         is_valid = False
    #         flash("Last name should be 1 to 50 characters long")

    #     # salary: must be an integer, positive, minimum of 40,000

    #     try:
    #         salary = int(data['salary'])
    #         if salary < 40000:
    #             is_valid = False
    #             flash("Salary should be at least 40,000")

    #     except:
    #         is_valid = False
    #         flash("Salary must be an integer greater than 40,000")

    #     # department must be selected
    #     if data['department_id'] == '-1':
    #         is_valid = False
    #         flash("Please select a department for this employee")

    #     return is_valid

    @staticmethod
    def validate_employee(data):

        first_name_regex = re.compile(r"^[A-Z]{1}[a-zA-Z. \-'!]{0,49}$")

        middle_and_last_name_regex = re.compile(r"^[a-zA-Z]{1}[a-zA-Z. \-'!]{0,49}$")

        is_valid = True

        # write validation logic here
        # must have a first name
        # first name 1 to 50 characters in length
        # start with capital letter
        # just letters, no numbers
        # special characters? ! - ' ' (a space) . '
        # 
        # l' 



        if not first_name_regex.match(data['first_name']):
            flash("First names should consist of 1 to 50 characters (alphabetical, spaces, dashes, apostraphes, exclamation points), starting with a capital letter.")
            is_valid = False

        # middle name is not needed, but if present
        # must also be 1 to 50 characters long
        # middle names follow same rules for first, but without the first
        # character being capitalized
        # also, we can assume first character is not special

        if data['middle_name'] != None:
            if not middle_and_last_name_regex.match(data['middle_name']):
                flash("Middle names should consist of 1 to 50 characters (alphabetical, spaces, dashes, apostraphes, exclamation points), starting with a letter.")
                is_valid = False

        
        # last name 1 to 50 characters
        # follow middle name rules

        if not middle_and_last_name_regex.match(data['last_name']):
            flash("Last names should consist of 1 to 50 characters (alphabetical, spaces, dashes, apostraphes, exclamation points), starting with a letter.")
            is_valid = False
        
        # salary: must be an integer, positive, minimum of 40,000

        try:
            salary = int(data['salary'])
            if salary < 40000:
                is_valid = False
                flash("Salary should be at least 40,000")

        except:
            is_valid = False
            flash("Salary must be an integer greater than 40,000")

        # department must be selected
        if data['department_id'] == '-1':
            is_valid = False
            flash("Please select a department for this employee")
       

        return is_valid
