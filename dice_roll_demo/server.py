from flask import Flask, render_template, redirect, request, session

from random import randint

app = Flask(__name__)
app.secret_key = "piouggawiuhpggqwfpiug"

@app.route('/')
def index():
    print(session)
    return render_template('index.html')

@app.route('/roll_dice', methods=['POST'])
def handle_dice():

    if f"sides_{request.form['dice_selector']}" not in session:
        session[f"sides_{request.form['dice_selector']}"] = []

    session[f"sides_{request.form['dice_selector']}"].insert(0, randint(1, int(request.form['dice_selector'])))

    session.modified = True

    return redirect('/')

@app.route('/reset_dice')
def reset_dice():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)