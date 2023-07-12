
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField , DateField , SelectField , IntegerField
from wtforms.validators import DataRequired

class EnterInfo(FlaskForm):
    Date = DateField(label = 'Date: ')
    VehicleNo = StringField(label = 'Vehicle No: ')
    Volume = StringField(label = 'Volume: ')
    Rate = StringField(label  = 'Rate: ')
    submit = SubmitField(label = 'ADD')
    option_entry = SelectField(label = 'Party' , choices=[('option1', 'SML'), ('option2', 'Pavitra'), ('option3', 'GCC')])
    product_entry = SelectField(label = 'Product' , choices=[('option1', 'Diesel') , ('option2', 'Petrol')])

class OptionForm(FlaskForm):
    option_name = StringField(label  = 'Party: ')
    option_value = option_name
    new_entry =  submit = SubmitField(label = 'New Entry')

