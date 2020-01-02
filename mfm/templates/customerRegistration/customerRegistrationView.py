from wtforms import Form, StringField, IntegerField, BooleanField,validators,SubmitField, widgets
from wtforms.validators import Email, DataRequired
from flask_wtf.file import FileField

class customerRegistration(Form):
    mobNum  =   IntegerField('Mobile Number', validators= [DataRequired()])
    cName   =   StringField('Customer Name', validators= [DataRequired()])
    cEmail  =   StringField('Customer Email', validators= [Email(), DataRequired()])
    cAddress=   StringField('Customer Address', validators= [DataRequired()])
    cID     =   FileField('Customer ID', validators= [DataRequired()])
    submit  =   SubmitField('Sign Up')
