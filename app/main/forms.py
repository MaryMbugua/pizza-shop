from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField
from wtforms.validators import Required,AnyOf

class PizzaForm(FlaskForm):
    name = StringField('Name of Pizza',validators=[Required()])
    description = StringField('Short Description of Pizza',validators=[Required()])
    price = StringField('Price of Pizza',validators=[Required()])
    category = RadioField('Pick from the following categories',choices=[('chicken','Chicken'),('beef','Beef'),('veg','Vegeterian')],validators=[Required()])
    size = SelectField(u'Pick from the following sizes',choices=[('sm','Small'),('md','Medium'),('lg','Large')],validators=[Required()])
    submit = SubmitField('Submit')