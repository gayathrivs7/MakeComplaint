import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

d = SQLAlchemy(app)

class Puppy(d.Model):

    __tablename__= 'puppies'  # overriding table name

    #creating cols for the puppies

    id   = d.Column(d.Integer,primary_key = True)
    name = d.Column(d.Text)
    age  = d.Column(d.Integer)


    def __init__(self,name,age):

        self.name = name
        self.age  = age

    def __repr__(self):

        return " Puppy {self.name} is {self.age} year/s old"




