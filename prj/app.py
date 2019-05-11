from flask import Flask, render_template,request,redirect,url_for
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


file =   '/home/gayathri/project/MakeComplaint/train.csv'   
nlp = spacy.load('en_core_web_md')
c = Complaint(file,nlp)


app = Flask(__name__)
Bootstrap(app)


@app.route('/login')
def enter():
    return render_template('login.html')


#Route login page
@app.route('/',methods = ['GET','POST'])
def log():
    return render_template('log.html')


@app.route('/success')
def take():

    category,dataset = c.department_class()

    dataset = preprocess.data_clean(dataset)

    dfwater,dfpwd,dfksrtc,dfkseb,dfenv = dataframes.dataframing(dataset)

    water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm = tokenise.tokenisation(dfwater,dfpwd,dfksrtc,dfkseb,dfenv)

    water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq = frequency.word_frequency(water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm)

    water_lis,pwd_lis,ksrtc_lis,kseb_lis,env_lis=topwords.most_repeated_keywords(dfwater,dfpwd,dfksrtc,dfkseb,dfenv,water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq,"manual")


    subject  =  request.args.get('subject')
    mess =  request.args.get('message')
    message  = subject + " "+ mess
    
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
    


    
    if subject and message:


        return render_template('Success.html',name =name,flags =flags)
    else:
        return redirect(url_for('log') )


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/know')
def info():
    return render_template('dataset.html')



if __name__ == '__main__':
    app.run(debug=True)
