from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user

from .. import db


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'



    return render_template('index.html',title=title)
