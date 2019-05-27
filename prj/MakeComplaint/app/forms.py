from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm
from wtforms import StringField,PasswordField,BooleanField,validators,SubmitField,RadioField,DateField,validators,SelectField
from wtforms.validators import DataRequired,input_required,optional,length,EqualTo
from wtforms import IntegerField
from wtforms.fields.html5 import DateField

class RegForm(DynamicForm):
  
    first_name = StringField(u'First Name', validators=[input_required()],widget=BS3TextFieldWidget()
        )
  
    last_name  = StringField(u'Last Name', validators=[input_required()],widget=BS3TextFieldWidget())
    aadhaar    = StringField(u'Aadhaar', [input_required(), length(min==12),length(max=12)],widget=BS3TextFieldWidget()
        )
    gender = SelectField('Gender', choices = [('M','Male'),('F','Female'),('T','Transgender')])
    dob = DateField("Date of Birth",format='%Y-%m-%d',validators=[input_required()])
    email = StringField("Email",validators=[DataRequired(),validators.Email()],widget=BS3TextFieldWidget()
        
        )
    number = IntegerField('Mobile',validators=[DataRequired([DataRequired()])])
    password   = PasswordField(' Password', [
               DataRequired(),
                EqualTo('confirm', message='Passwords must match')
                ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I Agree', [DataRequired()]
                )
    submit =SubmitField("Register")
