######################
#   Models.py        #
#####################

from sqlalchemy import Column, Integer, String,Date
from app import db
from flask_sqlalchemy import SQLAlchemy



class User(db.Model):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    aadhaar = Column(Integer,unique=True,nullable=False)
    name = Column(String(50),nullable=False)
    email = Column(String(120),nullable=False)
    dob = Column(Date,nullable=False)
    mobile=Column(Integer,nullable=False)
    password=Column(String(20),nullable=False)



    def __repr__(self):
        return '<User %r>' % (self.name)
db.create_all()
db.session.add(123456781011,'Gayathri','gayathri@gmail.com','1994-11-10',7907683839,'hare')
db.session.commit()
all_data=users.query.all()
for data in all_data:
    print(data)

    


