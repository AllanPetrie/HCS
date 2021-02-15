from app import app
from flask import render_template, request, send_from_directory, flash, redirect, url_for
import sys
import csv

#variants can either be colours or areas
VARIANT = 'colours'

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')



@app.route('/images')
def images():
    return render_template('images.html')

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

        return render_template('login.html', error=error)
