
# waiting for imports_1, please do not remove this line
from flask import render_template, redirect, url_for, request
from mfm import app
from mfm.templates.login.loginView import *
from mfm.authenticate import *
from mfm.templates.home.homeView import *
from mfm.templates.hotelDashboard.hotelDashboardView import *

import pdb

from mfm.Utility import *
from mfm.templates.customerRegistration.customerRegistrationView import *
# waiting for imports_2, please do not remove this line


@app.route('/')
@app.route('/home')
def home_def():
    return render_template('home/homeView.html')

@app.route('/login')
def login_def():
   return render_template('login/loginView.html')

@app.route('/hotelDashboard')
def hotelDashboard_def():
    data=Utility().getRoomInfo()
    return render_template('hotelDashboard/hotelDashboardView.html',data=data)

@app.route('/customerRegistration' ,methods = ['GET','POST'])
def customerRegistration_def():
    form = customerRegistration(request.form)
    if form.validate():
        return redirect(url_for('home_def'))
    return render_template('customerRegistration/customerRegistrationView.html',form=form)
