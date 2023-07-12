from rssbuddy import app
from flask import render_template , url_for , redirect , request 
from rssbuddy.models import SML
from rssbuddy import db
from rssbuddy.forms import EnterInfo , OptionForm

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/accounts/')
def account():
    optionform = OptionForm()
    if request.method == 'POST' and optionform.validate():
        print("Hello")  
        redirect(url_for('account'))

    return render_template('party.html' , optionform=optionform)

@app.route('/accounts/SML')
def sml_accounts():
    totalvolume = 0
    totalamount = 0 

    for item in SML.query.all():
        totalvolume = totalvolume + item.Volume

    for item in SML.query.all():
        totalamount = totalamount + item.Amount       

    sorted_rows = SML.query.order_by(SML.Date.asc()).all()

    return render_template('SML.html' , SMLAcc=sorted_rows, totalvolume=totalvolume,totalamount=totalamount)

@app.route('/accounts/add' , methods = ['POST','GET'])
def adding_acc():
    form = EnterInfo()

    if request.method == 'POST' and form.validate():
        if form.option_entry.data == 'option1' :
            if form.product_entry.data == 'option1':
                temp_product = 'Diesel'
            else:
                temp_product = 'Petrol'

            if temp_product == 'Diesel':
                Rate = 87.07 
            else:
                Rate = 101.06       

            created_field = SML(
                Date = form.Date.data,
                VehicleNo = form.VehicleNo.data,
                Volume = form.Volume.data,
                Amount = float(form.Volume.data) * 87.07,
                Rate = Rate,
                Product = temp_product
            )
            db.session.add(created_field)
            db.session.commit()
            return redirect(url_for('adding_acc'))
        

            
    return render_template('add.html',form=form)



