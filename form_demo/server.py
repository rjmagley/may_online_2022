from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "i am a flask project by instructor ryan"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/handle_results', methods = ['POST'])
def receive_form():

    session['full_name'] = request.form['full_name']
    session['maiden_name'] = request.form['mothers_maiden_name']
    session['first_pet'] = request.form['first_pet']
    session['ssn'] = request.form['social_security_number']
    return redirect('/show_results')

@app.route('/show_results')
def show_results():
    # print(session['full_name'])
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug = True)