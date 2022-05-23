from flask_app import app

from flask import render_template, redirect, request, flash, session

from flask_app.models.user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/register', methods=['POST'])
def register_user():

    # validate user
    if User.validate_user(request.form):
        data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        User.create_user(data)

    else:
        print("is not valid")

    # then if valid, add to DB

    return redirect('/')
@app.route('/users/login', methods = ['POST'])
def login_user():

    users = User.get_user_by_email(request.form)

    if len(users) != 1:
        flash("Incorrect email address")
        return redirect('/')

    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect password")
        return redirect('/')
    
    session['user_id'] = user.id
    session['username'] = user.username
    return redirect('/success')

@app.route('/success')
def success():
    if 'user_id' not in session:
        flash("You must be logged in to view this thing")
        return redirect('/')

    return render_template('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

