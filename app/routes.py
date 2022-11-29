from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    students = ['sean', 'kevon', 'duncan', 'alex']
    return render_template('index.html', name=students)

@app.route('/login')
def login():
    return 'this is a login page'

@app.route('/signup')
def signup():
    return 'this is a signup page'

