
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
    option_entry = SelectField(label = 'Party' , 
                              choices=[('option1', 'SML'), ('option2', 'Pavitra'), ('option3', 'GCC'),('option4',''),('option5',''),('option6',''),('option7',''),('option8',''),('option9',''),('option10','')])
    product_entry = SelectField(label = 'Product' , choices=[('option1', 'Diesel') , ('option2', 'Petrol')])

class OptionForm(FlaskForm):
    option_name = StringField(label  = 'Party: ')
    option_value = option_name
    new_entry = SubmitField(label = 'New Entry')

