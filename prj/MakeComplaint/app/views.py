from flask import render_template,flash,session
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi,SimpleFormView,expose


from . import appbuilder, db
from .models import Usertable
from .forms import RegForm
from .models import Usertable


'''class  Usertableview(ModelView):
    datamodel= SQLAInterface(Usertable)'''
    
class Usertableview(ModelView):
    datamodel = SQLAInterface(Usertable)


class MyFormView(SimpleFormView):
    
    form_title = "User Details"
    message = "Registered successfully"
    
    
    form = RegForm()
    if form.validate_on_submit():

        fname = form.first_name.data
        aadhaar= form.aadhaar.data
        lname=form.last_name.data
        gender=form.gender.data
        dob=form.dob.data
        email=form.email.data
        mobile=form.number.data
        password=form.password.data
        
        session['fname']= form.first_name.data
        session['aadhaar']= form.aadhaar.data
        session['lname']=form.last_name.data
        session['gender']=form.gender.data
        session['dob']=form.dob.data
        session['email']=form.email.data
        session['mobile']=form.number.data
        session['password']=form.password.data


        db.create_all()
        db.session.add(Usertable(aadhaar,fname,lname,gender,dob,email,mobile,password))
        db.session.commit()
        


  

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


#db.session.add(Usertable(aadhaar,fname,lname,gender,dob,email,mobile,password))


appbuilder.add_view(
    Usertableview,
    "User Info",
    icon="fa-folder-open-o",
    category="Info",
    category_icon="fa-envelope"
)
appbuilder.add_view(
    MyFormView,
    "My form View",
    icon="fa-group",
    label=("My form View"),
    category="Register",
    category_icon="fa-cogs",
)




