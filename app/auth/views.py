from flask import render_template,flash,request,url_for
from . import auth
from flask import render_template,redirect,url_for,abort
from .. import db
from ..models import Admin
from .forms import LoginForm,RegistrationForm

from flask_login import login_user,logout_user,login_required



@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Admin.query.filter_by(name=login_form.name.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.admin'))
        flash('Invalid username or Password')

    title = "pizza admin login"
    return render_template('auth/adminlogin.html', login_form=login_form, title=title)


@auth.route('/regester',methods = ['GET', 'POST'])
def regester():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Admin(name = form.name.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'New Account'

    return render_template('auth/adminregister.html', registration_form = form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth/adminlogin.html"))