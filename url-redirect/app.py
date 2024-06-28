from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def admin():
    return "Welcome BOSS"
@app.route('/guest/<guest_name>')
def guest(guest_name):
    return f'Hello {guest_name}, What do you want to do today!!!'
@app.route('/user/<user_name>')
def user(user_name):
    if user_name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest_name=user_name))

if __name__== '__main__':
    app.run(debug=True)