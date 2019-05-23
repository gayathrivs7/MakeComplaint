from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey,Date
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Usertable(Model):
    id =Column(Integer,primary_key=True)
    aadhaar=Column(Integer,nullable=False,unique=True)
    fname=Column(String(30),nullable=False)
    lname=Column(String(30),nullable=False)
    gender=Column(String(11),nullable=False)
    dob=Column(Date,nullable=False)
    email=Column(String(30),nullable=False)
    mobile=Column(Integer,nullable=False)
    password=Column(String(10),nullable=False)


    def __init__(self,aadhaar,fname,lname,gender,dob, email,mobile,password):
        self.aadhaar=aadhaar
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.dob=dob
        self.email=email
        self.mobile=mobile
        self.password=password

    def __repr__(self):
        return "{} {}".format(self.aadhaar,self.fname)
