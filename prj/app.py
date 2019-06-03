from flask import Flask, render_template,request,redirect,url_for,session
from Complaint  import Complaint
import spacy
import preprocess
from preprocess import data_clean #preprocess.py
import dataframes
from dataframes import dataframing
import tokenise
from tokenise import tokenisation
import frequency
from frequency import word_frequency
import testdata
from testdata import test
import topwords
from topwords import most_repeated_keywords
import predict
from predict import evaluate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,Date,Text,Boolean,ForeignKey
import os
from flask_migrate import Migrate
from sqlalchemy.orm import relationship


file =   '/home/gayathri/project/MakeComplaint/train.csv'   
nlp = spacy.load('en_core_web_md')
c = Complaint(file,nlp)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key=os.urandom(24)

#Db
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)
migrate = Migrate(app,db)
Bootstrap(app)
#taking form data from login page
def get_login_data():
    aadhaar = request.args.get('user')
    password = request.args.get('pass')
    print("Function")
    print(aadhaar)
    print(password)
    return aadhaar,password

#Route login page
@app.route('/',methods = ['GET','POST'])
def log():
    return render_template('log.html')

@app.route('/signin',methods = ['GET','POST'])
def enter():
    return render_template('signin.html')

@app.route('/success',methods=['GET','POST'])
def take():
    print("Take starting")

    category,dataset = c.department_class()

    dataset = preprocess.data_clean(dataset)

    dfwater,dfpwd,dfksrtc,dfkseb,dfenv = dataframes.dataframing(dataset)

    water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm = tokenise.tokenisation(dfwater,dfpwd,dfksrtc,dfkseb,dfenv)

    water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq = frequency.word_frequency(water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm)

    water_lis,pwd_lis,ksrtc_lis,kseb_lis,env_lis=topwords.most_repeated_keywords(dfwater,dfpwd,dfksrtc,dfkseb,dfenv,water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq,"manual")
    

    #subject  =  request.form['subject']
    subject  =  request.args.get('subject')
    mess =  request.args.get('message')
    #message =  request.form['message']

    message  = subject +" "+ mess

    keywords,item=testdata.test(message)

    water_flag,pwd_flag,kseb_flag,ksrtc_flag,env_flag,water_dept,pwd_dept,kseb_dept,ksrtc_dept,env_dept,flag_env,flag_kseb,flag_ksrtc,flag_pwd,flag_water= predict.evaluate(keywords,item,water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis,category,nlp)

    name= water_dept+pwd_dept+kseb_dept+ksrtc_dept+env_dept
    name = ['Water Authority','PWD',  'KSEB',  'KSRTC','Environment and climate change']
    flags= [0,1,2,3,4,5,6,7,8,9]
    flags[0]  = water_flag
    flags[1]  = pwd_flag
    flags[2]  = kseb_flag
    flags[3]  = ksrtc_flag
    flags[4]  = env_flag
    flags[5]  = flag_env
    flags[6]  = flag_kseb
    flags[7]  = flag_ksrtc
    flags[8]  = flag_pwd
    flags[9]  = flag_water
    

    #Prediction list
    predicted_class=[]
    if flags[0]==1:
        predicted_class.append(name[0])
    if flags[1]==1:
        predicted_class.append(name[1])
    if flags[2]==1:
        predicted_class.append(name[2])
    if flags[3]==1:
        predicted_class.append(name[3])
    if flags[4]==1:
        predicted_class.append(name[4])
    if flags[5]==1:
        predicted_class.append(name[4])
    if flags[6]==1:
        predicted_class.append(name[2])
    if flags[7]==1:
        predicted_class.append(name[3])
    if flags[8]==1:
        predicted_class.append(name[1])
    if flags[9]==1:
        predicted_class.append(name[0])

    print("Predicted class")
    print(predicted_class)
        
    print("Working >>>")

    #adding into database
    #taking aadhaar from database
    flag=0
    predicted_class_length=len(predicted_class)
    print("Predicted class length",predicted_class_length)
    for i in range(0,predicted_class_length):
        new_complaint = Complaints(subject=subject,content=mess,department=predicted_class[i])
        db.session.add(new_complaint)
        flag=flag+1
        db.session.commit()

        print('New Complaint submitted ')
    #all_data = Complaints.query.all()
    print("Flag Complaints length",flag)
    obj = db.session.query(Complaints).order_by(Complaints.comp_id.desc()).first()
    last_subject=obj.subject
    last_complaint=obj.content
    last_id=obj.comp_id

    notification = Notifications(comp_id=last_id,subject=last_subject,complaint=last_complaint)
    db.session.add(notification)
    db.session.commit()
    print("new notification added")

    #return render_template('Success.html',name =name,flags =flags)
    if subject and message:

        return render_template('Success.html',name=name,flags=flags,)
    else:
        return redirect(url_for('log'))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/know')
def info():
    return render_template('dataset.html')
'''@app.route('/department')
def depart():
    return render_template('department.html')'''

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

class User(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):

	    self.username = username
	    self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class Citizen(db.Model):
   
    id = Column(Integer, primary_key=True)
    aadhaar = Column(Integer,unique=True,nullable=False)
    name = Column(String(50),nullable=False)
    email = Column(String(120),nullable=False)
    #dob = Column(Date,nullable=False)
    mobile=Column(Integer,nullable=False)
    password=Column(String(20),nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Complaints(db.Model):

    comp_id = Column(Integer,primary_key=True)
    subject=Column(Text,nullable=False)
    content=Column(Text,nullable=False)
    department=Column(Text)
    #comp=db.relationship("Notifications")

    def __repr__(self):
        return '<Complaint %r>' %(self.subject)


class Notifications(db.Model):
    id = Column(Integer,primary_key=True)
    comp_id =Column(Integer)
    subject=Column(String(1000))
    complaint=Column(String(1000))
    viewed =Column(Boolean,default=False)

    def __repr__(self):
        print(self.id)



db.create_all()

'''wateradmin = User(username='wateradmin', password='wateradmin')
pwdadmin = User(username='pwdadmin', password='pwdadmin')
ksebadmin = User(username='ksebadmin', password='ksebadmin')
ksrtcadmin = User(username='ksrtcadmin', password='ksrtcadmin')
envadmin = User(username='envadmin', password='envadmin')'''

#user1 = Citizen(aadhaar=123456781011,name='Gayathri',email='gayathri@gmail.com',mobile=7907683839,password='hare')
#db.session.add(user1)
#db.session.commit()
#print("First user added to Citizen")

all_values=Citizen.query.all()
for data in all_values:
    print(data.aadhaar,data.name)
'''db.session.add(wateradmin)
db.session.add(pwdadmin)
db.session.add(ksebadmin)
db.session.add(ksrtcadmin)
db.session.add(envadmin)'''
db.session.commit()
print("Database created")
#fetching all the values in the table
all_values = User.query.all()
for a in all_values:
    print(a.username,a.password)
all_values=Citizen.query.all()
for i in all_values:
    print(i.aadhaar,i.password)

#user login
@app.route('/userlogin',methods = ['GET','POST'])
def userlogin():
    print("user login starting")
    if request.method == 'POST':

        username=request.form['user']
        password=request.form['pass']
        print("username",username)
        print("password",password)

        login_dept = User.query.all()
        login_user = Citizen.query.all()
        for i in login_user:
            print(type(i.aadhaar),i.password)
        user_list=[]
        dept_list=[]
        for i in login_user:
            i.aadhaar=str(i.aadhaar)
            if i.aadhaar==username and i.password==password:

                user_list.append(i.aadhaar)
                user_list.append(i.password)
                user_list.append(i.name)
                print("Adhaar",i.aadhaar)
                print("Password",i.password)
                 #return render_template('signin.html')



        for i in login_dept:
            if i.username ==username and i.password==password:
                dept_list.append(username)
                dept_list.append(password)

                print(i.username)
                print(i.password)
                session['depart']=password
                #return render_template('department.html',username=username)

        #print(login_dept)
        #Students.query.filter_by(city = ’Hyderabad’).all()

        print(user_list)
        print(dept_list)
        if len(user_list)!=0:

            return render_template('signin.html',)
        elif len(dept_list)!=0:

            return render_template('department.html',username=username)
        else:
            return render_template('invalid.html')
        
        
        '''if flag==1:

            return render_template('department.html',username=username)
        elif flag==0:
            return render_template('department.html',username=username)
        else:
            return render_template('invalid.html')'''



#user registration
@app.route('/register_data',methods = ['GET', 'POST'])
def registrationdata():
    if request.method == "POST":
        aadhaar=request.form['aadhaar']

        name = request.form['name']
        mob = request.form['mobile']
        password =request.form['password']
        #dob=request.form['dob']
        #date=request.form['date']
        email=request.form['email']

        new_user = Citizen(aadhaar=aadhaar,name=name,email=email,mobile=mob,password=password)
        db.session.add(new_user)
        db.session.commit()
        print("New user added")
        
        user1=Citizen.query.all()
        for user in user1:
            print(user.name,user.aadhaar)
        print(user1)
        '''#inserting Citizen username and password into USer table
        new_user = User(username=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        print("Data added to user table")
        user1=User.query.all()
        for user in user1:
            print(user.name,user.aadhaar)
        print(user1)'''


        return "helo"

#Group Complaints
from bs4 import BeautifulSoup
@app.route('/groupComplaints')
def group_complaints():
    username=User.query.all()
    usernames=[]
    departments=['PWD ','Water Authority','Environment and climate change','KSEB','KSRTC']
    
    for i in username:
        usernames.append(i.username)
    #grouping complaints
    waterdata=Complaints.query.filter(Complaints.department=='Water Authority')
    pwddata=Complaints.query.filter(Complaints.department=='PWD')
    envdata=Complaints.query.filter(Complaints.department=='Environment and climate change')
    ksebdata=Complaints.query.filter(Complaints.department=='KSEB')
    ksrtcdata=Complaints.query.filter(Complaints.department=='Water Authority')
    username=session['depart']
    print("session",username)
    water_id=[]
    water_subject=[]
    water_content=[]
    water_department=[]
    for i in waterdata:
        water_id.append(i.comp_id)
        water_subject.append(i.subject)
        water_content.append(i.content)
        water_department.append(i.department)
    length=len(water_id)

    if username=='wateradmin':
        return render_template('group_table.html',length=length,water_id=water_id,water_subject=water_subject,water_content=water_content,water_department=water_department)

    '''for i in waterdata:

        print(i.subject,i.content,i.department)
    

    return render_template('department.html')'''
    

#shows complaint records 
@app.route('/shownotifications')
def show_notifications():
    all_data = Complaints.query.all()
    complaints_id_list=[]
    complaints_subject_list=[]
    complaints_content_list=[]
    complaint_department=[]

    for i in all_data:
       #print(i.id,i.subject,i.content)
       complaints_id_list.append(i.comp_id)
       complaints_subject_list.append(i.subject)
       complaints_content_list.append(i.content)
       complaint_department.append(i.department)

    
    length=len(complaints_content_list)
    
    return render_template('table.html',_anchor='myanchor',length=length,complaints_id_list=complaints_id_list,complaints_subject_list=complaints_subject_list,complaints_content_list=complaints_content_list,complaint_department=complaint_department)
  
#submit complaint
'''@app.route('/submit',methods=['GET','POST'])
def submit():
    print("Submit function entering")
    if request.method=='GET':
        subject  =request.form['subject']
        complaint =request.form['message']

        print(subject,complaint)
        return redirect(url_for('take'))'''


if __name__ == '__main__':
    app.run(debug=True)