from rssbuddy import app
from flask import render_template , url_for , redirect , request 
from rssbuddy.models import party_record , Records
from rssbuddy import db
from rssbuddy.forms import EnterInfo , OptionForm



@app.route('/', methods = ['GET','POST'])
def home_page():
    form = EnterInfo()
    
    if request.method == 'POST' :
        party_name = form.option_entry.data
        return redirect(url_for('records', party_name=party_name))

    parties = party_record.query.all()
    form.option_entry.choices = [(party.name, party.name) for party in parties]    
    return render_template('home.html',form=form)



@app.route('/accounts/',methods = ['POST','GET'])
def account():
    optionform = OptionForm()


    if request.method == 'POST' and optionform.validate():
        temp_party = party_record(name = optionform.option_name.data )
        db.session.add(temp_party)
        db.session.commit()
        return redirect(url_for('account'))
    

    return render_template('party.html' , optionform=optionform )

@app.route('/accounts/add' , methods = ['POST','GET'])
def adding_acc():
    form = EnterInfo()  
    options = party_record.query.all()
    form.option_entry.choices = [(option.name , option.name) for option in options]

    if request.method == 'POST' :
            if form.product_entry.data == 'option1':
                temp_product = 'Diesel'
            else:
                temp_product = 'Petrol'

            if temp_product == 'Diesel':
                Rate = 87.07 
            else:
                Rate = 101.06       

            created_field = Records(
                Party = form.option_entry.data,
                Date = form.Date.data,
                VehicleNo = form.VehicleNo.data,
                Volume = form.Volume.data,
                Amount = float(form.Volume.data) * 87.07,
                Rate = Rate,
                Product = temp_product
            )
            print(created_field.Rate)
            db.session.add(created_field)
            db.session.commit()
            return redirect(url_for('adding_acc'))

    return render_template('add.html',form=form)



@app.route('/records', methods = ['POST','GET'])
def records():
    partyname = request.args.get('party_name')
    bill_records = db.session.query(Records).filter_by(Party=partyname).all()

    return render_template('billrecords.html',bill_records=bill_records,partyname=partyname)
    




