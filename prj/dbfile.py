from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask('__name__')

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False

db = SQLAlchemy(app)

Migrate(app,db)

class Users(db.Model):
     __tablename__ = 'User'  #table name

     #creating columns 
     id          = db.Column(db.Integer,primary_key = True)
     name        = db.Column(db.Text)
     username    = db.Column(db.Text, unique=True)
     password    = db.Column(db.Text)

     def __init__(self,id,name,username,email,password):
         self.id        = id
         self.name      = name
         self.username  = username         
         self.password  = password

     def __repr__(self):
        return "{} {} {} {} {}".format(self.id,self.name,self.username,self.email,self.password)






