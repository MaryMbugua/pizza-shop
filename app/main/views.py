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

       
    chicken = Availablepizza.query.filter_by(category='chicken').all()

    beef = Availablepizza.query.filter_by(category='beef').all()
  
    vegetable = Availablepizza.query.filter_by(category='veg').all()


    return render_template('index.html',title=title,beef=beef,vegetable=vegetable,chicken=chicken)


@main.route('/admin',methods = ['GET','POST'])
def admin():
    '''
    View root page function that returns the index page and its data
    '''
    pizzaform = PizzaForm()
    if pizzaform.validate_on_submit():
        pizza = Availablepizza(img_url= pizzaform.img_url.data,name= pizzaform.name.data,category= pizzaform.category.data,description= pizzaform.description.data,price= pizzaform.price.data,size= pizzaform.size.data)
        
        pizza.save_availablepizzas()

        return redirect (url_for('main.admin'))
        

    return render_template('admin.html',pizzaform=pizzaform)





