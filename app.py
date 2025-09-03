from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
import pytz
import os
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv   # For hiding Secrets 

# Load environment variables from .env
load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Secret key from .env  # Required for flash and sessions

# MongoDB connection
# MongoDB connection from .env
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# Database and Collection setup
db = client.login_app  
users = db.login        # Collection name


# Home Page - index page
@app.route('/')
def index():
    if 'user' in session:
        return render_template("index.html", username=session['user'])
    return redirect(url_for('login'))


# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if users.find_one({'username': username}):
            flash("Username already exists!", "danger")
            return redirect(url_for('signup'))

        hashed_pw = generate_password_hash(password)
        users.insert_one({'username': username, 'password': hashed_pw})
        flash("Signup successful! Please login.", "success")
        return redirect(url_for('login'))
    return render_template('signup.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        remember = request.form.get('remember')

        user = users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['user'] = username

            # If "Remember Me" is checked, set cookie
            resp = make_response(redirect(url_for('index')))
            if remember:
                resp.set_cookie('remember_token', username, max_age=60*60*24*7)  # 7 days
            return resp
        else:
            flash("Invalid username or password!", "danger")
            return redirect(url_for('login'))

    # Auto login using remember me cookie
    remember_token = request.cookies.get('remember_token')
    if remember_token and users.find_one({'username': remember_token}):
        session['user'] = remember_token
        return redirect(url_for('index'))

    return render_template('login.html')


# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('remember_token', '', expires=0)  # Clear cookie
    flash("You have been logged out.", "info")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
