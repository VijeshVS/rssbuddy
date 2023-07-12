from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , DateField , SelectField , IntegerField , FormField , FieldList
from wtforms.validators import DataRequired

class EnterInfo(FlaskForm):
    Date = DateField(label = 'Date: ')
    VehicleNo = StringField(label = 'Vehicle No: ')
    Volume = StringField(label = 'Volume: ')
    Rate = StringField(label  = 'Rate: ')
    submit = SubmitField(label = 'ADD')
    go = SubmitField(label = 'GO')
    option_entry = SelectField(label = 'Party List: ', choices=[])
    product_entry = SelectField(label = 'Product' , choices=[('option1', 'Diesel') , ('option2', 'Petrol')])

class OptionForm(FlaskForm):
    option_name = StringField(label  = 'Party: ')
    option_value = option_name
    new_entry = SubmitField(label = 'New Entry')
    date1 = DateField(label = 'From: ')
    date2 = DateField(label = 'To: ')

class AmtRec(FlaskForm):
    Date = DateField(label = 'Date: ')
    Amount = StringField(label = 'Amount Received: ')
    submit = SubmitField(label = 'ADD')