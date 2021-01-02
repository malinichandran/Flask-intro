from flask import Flask,request
app= Flask(__name__)

@app.route('/welcome')
def welcome_page():
    return f"<h1>Welcome</h1>"

@app.route('/welcome/home')
def home_page():
    return f"<h1>Welcome Home</h1>"

@app.route('/welcome/back')
def back_page():
    return f"<h1>Welcome Back</h1>"