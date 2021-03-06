from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    first_name =db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
  

    def __repr__(self):
        return f'User {self.username}'
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic") 

class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'
    id=db.Column(db.Integer,primary_key = True)
    name=db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

class Availablepizza(UserMixin,db.Model):
    __tablename__= 'availablepizzas'
    id=db.Column(db.Integer,primary_key= True)
    name=db.Column(db.String(255))
    description=db.Column(db.String(255))
    price=db.Column(db.String(255))
    category=db.Column(db.String(255))
    size=db.Column(db.String(255))
    image_path=db.Column(db.String())
    img_url=db.Column(db.String(255))


    def __repr__(self):
        return f'{self.name}'

    def save_availablepizzas(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_categories(cls, category):
        pizza_cat = availablepizzas.query.filter_by(category=category)
        return pizza_cat

    # def  __init__(self,id,name,description,price,category,size,image_path):
    #     self.ca