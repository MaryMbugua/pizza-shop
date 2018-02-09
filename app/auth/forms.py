from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import Admin, User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    name = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if Admin.query.filter_by(name =data_field.data).first():
                raise ValidationError('There is an account with that name')

class LoginForm(FlaskForm):
    name = StringField('Your name',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class User_regestrationForm(FlaskForm):
    username = StringField('Enter your username',validators = [Required()])
    firstname = StringField('Enter your firstname',validators = [Required()])
    email = StringField('Enter your email',validators=[Required()])
    lastname = StringField('Enter your lastname',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')
            
class User_loginForm(FlaskForm):
    email = StringField('Your email address',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')