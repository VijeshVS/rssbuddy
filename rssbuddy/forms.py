from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , DateField , SelectField , IntegerField , FormField , FieldList , PasswordField , validators
from wtforms.validators import DataRequired , EqualTo , ValidationError

class EnterInfo(FlaskForm):
    Date = DateField(label = 'Date: ',validators=[DataRequired()])
    VehicleNo = StringField(label = 'Vehicle No: ')
    Volume = StringField(label = 'Volume: ',validators=[DataRequired()])
    Rate = StringField(label  = 'Rate: ')
    submit = SubmitField(label = 'ADD')
    go = SubmitField(label = 'GO')
    option_entry = SelectField(label = 'Party List: ', choices=[])
    product_entry = SelectField(label = 'Product' , choices=[('option1', 'Diesel') , ('option2', 'Petrol')])

class OptionForm(FlaskForm):
    option_name = StringField(label  = 'Party: ', validators=[DataRequired()])
    option_value = option_name
    new_entry = SubmitField(label = 'New Entry')
    date1 = DateField(label = 'From: ')
    date2 = DateField(label = 'To: ')
    go = SubmitField(label = 'GO')

class AmtRec(FlaskForm):
    Date = DateField(label = 'Date: ',validators=[DataRequired()])
    Amount = StringField(label = 'Amount Received: ',validators=[DataRequired()])
    submit = SubmitField(label = 'ADD')


class cngform(FlaskForm):
    Date = DateField(label = 'Date: ',validators=[DataRequired()])
    aside = StringField(label = 'A side reading: ',validators=[DataRequired()])
    bside = StringField(label = 'B side reading: ',validators=[DataRequired()])
    Rate = StringField(label  = 'Rate: ')
    submit = SubmitField(label = 'ADD')

class LoginForm(FlaskForm):
    username = StringField(label = 'Username: ', validators=[DataRequired()])
    password = PasswordField(label = 'Password: ' , validators=[DataRequired()])
    submit = SubmitField(label = 'Login')

class RegisterForm(FlaskForm):
    username = StringField(label = 'Username: ',validators=[DataRequired()])
    password1 = PasswordField(label = 'Password: ',validators=[DataRequired()])
    password2 = PasswordField(label = 'Confirm Password: ',validators=[DataRequired(),EqualTo('password1')])
    submit = SubmitField(label = 'Create Account')

class DeleteForm(FlaskForm):
    submit = SubmitField(label = 'Delete')

class Print(FlaskForm):
    submit = SubmitField(label = 'View Printable Format')

class UpdateForm(FlaskForm):
    Date = DateField(label = 'Date: ', validators=[DataRequired()])
    VehicleNo = StringField(label = 'Vehicle No: ', validators=[DataRequired()])
    Volume = StringField(label = 'Volume: ', validators=[DataRequired()])
    product_entry = SelectField(label = 'Product' , choices=[('option1', 'Diesel') , ('option2', 'Petrol')])
    submit = SubmitField(label = 'Update')
