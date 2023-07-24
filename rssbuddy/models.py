from rssbuddy import db
import csv

class Records(db.Model):
    Party = db.Column(db.String(length = 10), nullable=False)
    ID = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.Date(), nullable=False)
    VehicleNo = db.Column(db.String(length = 20))
    Volume = db.Column(db.Integer(), nullable=False)
    Rate = db.Column(db.Integer(), nullable=False)
    Product = db.Column(db.String(length = 10), nullable=False)
    Amount = db.Column(db.Integer(), nullable=False)

'''
    @classmethod 
    def instantiate_from_csv(cls):
        from datetime import datetime
        with open('items.csv','r') as f:
              reader = csv.DictReader(f)
              items = list(reader)
              
        for item in items:
             
             temp_rec = Records(Party = item.get('party'),
                     Date = datetime.strptime(item.get('date'), '%d-%m-%Y').date(),
                     VehicleNo = item.get('vehicleno'),                   
                     Volume = item.get('volume'),
                     Rate = item.get('rate'),
                     Product = item.get('product'),
                     Amount = item.get('amount'))
             
             db.session.add(temp_rec)
             db.session.commit()  

             '''          

class party_record(db.Model)   :
    name = db.Column(db.String(length = 10))
    ID = db.Column(db.Integer(), primary_key=True)

class AmountRecord(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    AmtDate = db.Column(db.String(length = 10), nullable=False)
    Amount = db.Column(db.Integer(), nullable=False)
    AmtParty =  db.Column(db.String(length = 10), nullable=False)

class CNG_record(db.Model): 
      ID = db.Column(db.Integer(), primary_key=True)
      cngdate = db.Column(db.Date())
      aside = db.Column(db.String(length = 10), nullable=False)
      bside = db.Column(db.String(length = 10), nullable=False)
      total = db.Column(db.String(length = 10), nullable=False)
      cngrate = db.Column(db.Integer(), nullable=False)
      cngamt = db.Column(db.Integer(), nullable=False)



    


