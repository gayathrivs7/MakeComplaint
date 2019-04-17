
from flask import Flask, render_template,request,redirect,url_for
import complaint




app = Flask(__name__)

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/success')
def take():

    subject  =  request.args.get('subject')
    mess =  request.args.get('message')
    message  = subject + " "+ mess

    if subject and message:

        return render_template('Success.html',message=message)
    else:
        return redirect(url_for('log') )



if __name__ == '__main__':
    app.run()
