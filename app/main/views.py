from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .forms import PizzaForm
from ..models import Availablepizza
from .. import db


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'



    return render_template('index.html',title=title)


@main.route('/admin')
def admin():
    '''
    View root page function that returns the index page and its data
    '''
    pizzaform = PizzaForm()
    if pizzaform.validate_on_submit():
        pizza = Pizza(name= pizzaform.name.data,category= pizzaform.category.data,description= pizzaform.description.data,price= pizzaform.price.data,image= pizzaform.image.data,size= pizzaform.size.data)



    return render_template('admin.html',pizzaform=pizzaform)





