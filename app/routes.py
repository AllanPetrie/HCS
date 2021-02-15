from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')


@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/login')
def index():
    return render_template('login.html')



@app.route('/imageselect')
def imageselect():
    return render_template('gregor.html')
