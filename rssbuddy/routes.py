from rssbuddy import app
from flask import render_template , url_for , redirect , request ,flash, get_flashed_messages 
from rssbuddy.models import party_record , Records , AmountRecord , CNG_record , User
from rssbuddy import db 
from rssbuddy.forms import EnterInfo , OptionForm , AmtRec , cngform , LoginForm , RegisterForm , DeleteForm , UpdateForm , Print
from datetime import datetime
from flask_login import login_user , login_required , current_user , logout_user

@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/accounts/', methods = ['GET','POST'])
@login_required
def home_page():
    form = EnterInfo()
    opform = OptionForm()
    
    if request.method == 'POST' :
        date1 = opform.date1.data
        date2 = opform.date2.data
        print(date1)
        if date1 == None:
            date1 = datetime.strptime('1-06-2005', '%d-%m-%Y').date()

        if date2 == None:
            date2 = datetime.strptime('1-06-2050', '%d-%m-%Y').date()    
            
        party_name = form.option_entry.data
        return redirect(url_for('records', party_name=party_name,date1=date1,date2=date2))

    parties = party_record.query.all()
    form.option_entry.choices = [(party.name, party.name) for party in parties]    
    return render_template('home.html',form=form,opform=opform)




@app.route('/accounts/party',methods = ['POST','GET'])
@login_required
def account():
    optionform = OptionForm()

    if request.method == 'POST' and optionform.validate():
        # check duplicate 
        check_party = party_record.query.filter_by(name = optionform.option_name.data).first()
        if check_party:
            flash(f'{check_party.name} already exists !!' , category='danger')
            return redirect(url_for('account'))
        else:    
            temp_party = party_record(name = optionform.option_name.data )
            db.session.add(temp_party)
            db.session.commit()
            flash(f'Added {temp_party.name} successfully !!' , category='success')
            return redirect(url_for('account'))
    
    if request.method == 'GET':
        return render_template('party.html' , optionform=optionform )


@app.route('/accounts/add' , methods = ['POST','GET'])
@login_required
def adding_acc():
    #Records.instantiate_from_csv()
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
                Amount = float(form.Volume.data) * float(Rate),
                Rate = Rate,
                Product = temp_product
            )
            print(created_field.Rate)
            db.session.add(created_field)
            db.session.commit()
            flash(f'Added bill to {created_field.Party} successfully !!',category='success')
            return redirect(url_for('adding_acc'))

    if request.method == 'GET':
        return render_template('add.html',form=form)



@app.route('/records', methods = ['POST','GET'])
def records():

    partyname = request.args.get('party_name')
    fromdate = request.args.get('date1')
    todate = request.args.get('date2')

    print = Print()
    deleteform = DeleteForm()
    updateform = UpdateForm()

    if request.method == 'POST' :
        bill_id = request.form.get('record_item')
        bill_object = Records.query.filter_by( ID = bill_id ).first()
        if bill_object:
            db.session.delete(bill_object)
            db.session.commit()
            date = bill_object.Date.strftime('%d/%m/%Y')
            flash(f'{date} | {bill_object.Party} | {bill_object.VehicleNo} | {bill_object.Volume} L , Bill deleted successfully' , category = 'success')  
            return redirect(url_for('home_page'))
        
        billup_id = request.form.get('update_item')
        billup_object = Records.query.filter_by( ID = billup_id ).first()
        if billup_object:
            billup_object.Date = updateform.Date.data
            billup_object.VehicleNo = updateform.VehicleNo.data
            billup_object.Volume = updateform.Volume.data

            if updateform.product_entry.data == 'option1':
                temp_product = 'Diesel'
            else:
                temp_product = 'Petrol'

            if temp_product == 'Diesel':
                Rate = 87.07 
            else:
                Rate = 101.06

            billup_object.Product = temp_product
            billup_object.Rate = Rate
            billup_object.Amount = float(Rate)*float(updateform.Volume.data)
            db.session.commit()
            date01 = billup_object.Date.strftime('%d/%m/%Y')
            flash(f'Bill changed to -> {date01} | {billup_object.Party} | {billup_object.VehicleNo} | {billup_object.Volume} L , Bill updated successfully' , category = 'success')   
            return redirect(url_for('home_page'))

        # fix this later
        return redirect(url_for('printable_page',partyname=partyname,
                                fromdate=fromdate,todate=todate))
    


    if request.method == 'GET':
        amt_bills = AmountRecord.query.filter(AmountRecord.AmtParty == partyname)
        amt_bills_total=0

        for amt in amt_bills:
            amt_bills_total += amt.Amount
    
        

        bill_records = Records.query.filter(
        Records.Date.between(fromdate, todate),
        Records.Party == partyname)
        # bill_records = db.session.query(Records).filter_by(Party=partyname).all()
        totalvolume=0
        totalamount=0


        for bill in bill_records:
            totalvolume += bill.Volume
            totalamount += bill.Amount

        balance = float(totalamount) - float(amt_bills_total)     

        return render_template('billrecords.html',
                            bill_records=bill_records,partyname=partyname,
                            totalvolume=totalvolume,totalamount=totalamount,
                            amt_bills_total=amt_bills_total,amt_bills=amt_bills,balance=balance,
                            deleteform=deleteform,updateform=updateform,print=print)
    

@app.route('/print_record',methods = ['POST','GET'])
def printable_page():

    fromdate = request.args.get('fromdate')
    todate = request.args.get('todate')
    partyname = request.args.get('partyname')

    fromdate = datetime.strptime(fromdate, '%Y-%m-%d').date()
    todate = datetime.strptime(todate, '%Y-%m-%d').date()

    print(fromdate,todate,partyname)

    bill_records = Records.query.filter(Records.Date.between(fromdate, todate), Records.Party == partyname)
    
    # bill_records = db.session.query(Records).filter_by(Party=partyname).all()
    totalvolume=0
    totalamount=0


    for bill in bill_records:
        totalvolume += bill.Volume
        totalamount += bill.Amount

    return render_template('printable_record.html',totalamount=totalamount,totalvolume=totalvolume,partyname=partyname,bill_records=bill_records,
                           fromdate=fromdate,todate=todate)    



@app.route('/accounts/amtrec',methods = ['POST','GET'])
@login_required
def amount_rec():
    amt_form = AmtRec()
    form = EnterInfo()
    options = party_record.query.all()
    form.option_entry.choices = [(option.name , option.name) for option in options]


    if request.method == 'POST' :
        temp_rec = AmountRecord(AmtDate = amt_form.Date.data ,
                          Amount = amt_form.Amount.data ,
                           AmtParty = form.option_entry.data )
        db.session.add(temp_rec)
        db.session.commit()
        flash(f'Amount added to {temp_rec.AmtParty} successfully !!' , category='success')
        return redirect(url_for('amount_rec'))
    

    if request.method == 'GET':
        return render_template('amtrec.html',amt_form=amt_form,form=form)

@app.route('/cng/addcng',methods = ['POST', 'GET'])
@login_required
def add_cng():
    Cngform = cngform()
    if request.method == 'POST':
        cngtotal = float(Cngform.aside.data)+float(Cngform.bside.data)
        cngrate = float(Cngform.Rate.data)
        temp_record = CNG_record(cngdate = Cngform.Date.data,
                                 aside = Cngform.aside.data,
                                 bside = Cngform.bside.data,
                                 total = float(Cngform.aside.data) + float(Cngform.bside.data),
                                 cngrate = float(Cngform.Rate.data),
                                 cngamt = cngrate*cngtotal )
        db.session.add(temp_record)
        db.session.commit()
        flash('CNG sales added successfully',category='success')
        return redirect(url_for('add_cng'))
    
    if request.method == 'GET':
        return render_template('cngadd.html',cngform=Cngform)


@app.route('/cng/',methods = ['POST','GET'])
@login_required
def cng_home():

    hello = Records.query.all()
    
    for bill in hello:
        bill.Amount = bill.Volume * bill.Rate
        db.session.commit()

    opform = OptionForm()
    if request.method == 'POST':
        cngdate1 = opform.date1.data
        cngdate2 = opform.date2.data
        return redirect(url_for('cng_records',cngdate1=cngdate1,cngdate2=cngdate2))

    if request.method == 'GET':
        return render_template('cnghome.html',opform=opform)    



@app.route('/cngrecords', methods = ['POST','GET'])
def cng_records():
    fromdate = request.args.get('cngdate1')
    todate = request.args.get('cngdate2')
    bill_records = CNG_record.query.filter(
    CNG_record.cngdate.between(fromdate, todate))
    # bill_records = db.session.query(Records).filter_by(Party=partyname).all()
    totalvolume=0
    totalamount=0
    
    for bill in bill_records:
        totalvolume += float(bill.total)
        totalamount += float(bill.cngamt)

    return render_template('cngbillrecords.html',
                           bill_records=bill_records,totalvolume=totalvolume,
                           totalamount=totalamount)

@app.route('/register',methods = ['POST','GET'])
def register_page():
    registerform = RegisterForm()
    if request.method == 'POST':
        temp_user = User( username = registerform.username.data,
                         password = registerform.password1.data)
        db.session.add(temp_user)
        db.session.commit()
        login_user(temp_user)
        flash(f'Account created successfully !! Now you are logged in as {temp_user.username}',category='success')
        return redirect(url_for('home_page'))
    
    if request.method == 'GET':
        return render_template('register.html',registerform=registerform)




@app.route('/login',methods = ['POST','GET'])
def login_page():
    loginform = LoginForm()
    if request.method == 'POST' :
        temp_user = User.query.filter_by(username = loginform.username.data).first()
        if temp_user and temp_user.check_password_correction(try_password=loginform.password.data):
            login_user(temp_user)
            flash(f'Logged in as {temp_user.username} successfully !!', category = 'success')
            return redirect(url_for('home_page'))

    if request.method == 'GET':
        return render_template('login.html',loginform=loginform)



@app.route('/base')
def base_page():
    return render_template('base.html')


@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'Successfully logged out !', category = 'info')
    return redirect(url_for('home'))


