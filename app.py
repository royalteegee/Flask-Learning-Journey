import os
from flask import Flask, redirect, url_for, request, render_template, flash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')  # Set a secret key for session management

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            flash('Login Successful!', 'success')
            return redirect(url_for('success'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/success')
def success():    
    return 'Login Successful!'

if __name__ == '__main__':
    app.run(debug=True)
