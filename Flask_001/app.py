# this is a simple register and login flask app
# a user can register and login with a username and password
from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3 # for database
import bcrypt # for password hashing

app = Flask(__name__)
app.secret_key = 's3cr3t'


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def init_db():
    with app.app_context():
        db = sqlite3.connect('userstable.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT''')
        db.commit()

@app.route('/') #route() decorater binds a function to a URL
def home():  # this function is executed when the user visits the home page
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password) # hash the password
        try:
            with sqlite3.connect('userstest.db') as db:  # create a connection to the database
                cursor = db.cursor()
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
                db.commit()  #commit the changes
            flash('registered successfully!', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!', 'danger')
        return render_template('register.html')

    @app.route


if __name__ == '__main__':
    app.run(debug=True)