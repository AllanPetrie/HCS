from app import app
from flask import render_template, request, send_from_directory, flash, redirect, url_for
import sys
import csv

#variants can either be colours or areas
VARIANT = 'colours'

@app.route('/')
@app.route('/index')
def index():
    return render_template('register.html')

@app.route('/images')
def images():
    return render_template('images.html')

#this whole function is useless. Delete
@app.route('/authenticatePassword', methods=['POST'])
def authenticatePassword():
   
    error = None
    userfound = False

    if request.method == 'POST':

        form_data = request.form

        #very very bad way of handling authetication
        with open('./password_creds.csv') as pwrds:

            #read in password csv
            reader = csv.DictReader(pwrds)  
                
            #iterate over it to find a match
            for line in reader:
                if line['username'] == form_data['username']:
                    userfound = True
                    actual = line['password']
                    entered = form_data['password']
                    if line['password'] == form_data['password']: 
                        
                        #redirect to different pages based on variant
                        if VARIANT == 'colours':
                            return redirect(url_for('images'))
                        if VARIANT == 'area':
                            return "area login"

                    else:
                        error = "Wrong password." 
                        break

        if form_data['username'] == '' and form_data['password'] == '':
            error = "No username or password has been entered."
        elif form_data['username'] == '':
            error = "No username has been entered."
        elif form_data['password'] == '':
            error = "No password has been entered."
        elif not userfound:
            error = "Username not found."

        if error:
            error += " Please try again."
        
        session['username'] = form_data['username']
        return render_template('login.html', error=error)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_images')
def register_images():
    return render_template('register_images.html')

@app.route('/register_points')
def register_points():
    return render_template('register_points.html')

@app.route('/addUserAccount', methods=['POST'])
def addUserAccount():
    
    error = None
    
    if request.method == 'POST':

        form_data = request.form

        #check account doesn't already exist
        uname = form_data['username']
        with open('./password_creds.csv') as pwrds:

            reader = csv.DictReader(pwrds)  
            for line in reader:
                if line['username'] == uname:
                    error = "Account with username " + uname + " already exists."
                    return render_template('register.html', error=error)


            #check that passwords match
            if form_data['password'] != form_data['confirm']:
                error = "Passwords don't match."
                return render_template('register.html', error=error)
            
            #now add username and password to ""database""

        with open('./password_creds.csv', 'a') as pwrds:
            writer = csv.writer(pwrds)
            writer.writerow([uname, form_data['password']]) 

        session['username'] = uname
        session['password'] = form_data['password']
        return render_template('register_images.html')

        
@app.route('/imageselect')
def imageselect():
    return render_template('gregor.html')
