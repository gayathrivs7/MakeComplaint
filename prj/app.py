
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

file =   '/home/gayathri/project/MakeComplaint/data.csv'   
nlp = spacy.load('en_core_web_md')
c = Complaint(file,nlp)


app = Flask(__name__)

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/success')
def take():

    category,dataset = c.department_class()

    dataset = preprocess.data_clean(dataset)

    dfwater,dfpwd,dfksrtc,dfkseb,dfenv = dataframes.dataframing(dataset)

    water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm = tokenise.tokenisation(dfwater,dfpwd,dfksrtc,dfkseb,dfenv)

    water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq = frequency.word_frequency(water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm)




    subject  =  request.args.get('subject')
    mess =  request.args.get('message')
    message  = subject + " "+ mess

    if subject and message:

        return render_template('Success.html',message=message)
    else:
        return redirect(url_for('log') )



if __name__ == '__main__':
    app.run()
