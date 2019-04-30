import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Integer,Column,String
from flask_migrate import Migrate





basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__= 'puppies'  # overriding table name

    #creating cols for the puppies

    id   = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80))
    age  = db.Column(db.Integer)
    breed = db.Column(db.Text)
    color  = db.Column(db.Text)


    def __init__(self,name,age,breed,color):

        self.name = name
        self.age  = age
        self.breed = breed
        self.color = color

    def __repr__(self):

        return "Puppy {} is {} years old is {} is in {} color".format(self.name,self.age,self.breed,self.color)




