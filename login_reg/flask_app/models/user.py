from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re

class User():

    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (username, email, password) VALUES (%(username)s, %(email)s, %(password)s);"

        result = connectToMySQL("login_may_2022").query_db(query, data)

        return result

    @classmethod
    def get_user_by_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"

        results = connectToMySQL("login_may_2022").query_db(query, data)

        users = []

        for item in results:
            users.append(User(item))

        return users

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        results = connectToMySQL("login_may_2022").query_db(query, data)

        users = []

        for item in results:
            users.append(User(item))

        return users

    @staticmethod
    def validate_user(data):

        is_valid = True

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # username must be of valid length

        if len(data['username']) < 3 or len(data['username']) > 20:
            is_valid = False
            flash("Username must be at least 3 characters, up to 20 characters")

        # username must be unique
        if len(User.get_user_by_username(data)) != 0:
            is_valid = False
            flash("Username already in use")
       

        # email must follow pattern
        if not email_regex.match(data['email']):
            is_valid = False
            flash("Please provide a valid user email")

        # email must be unique
        if len(User.get_user_by_email(data)) != 0:
            is_valid = False
            flash("Email already in use")

        # password must be at least 8 characters
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters")

        # password and confirm_password fields must match
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Password and confirm password must match exactly")

        return is_valid