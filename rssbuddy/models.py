from rssbuddy import db , bcrypt
import csv
from flask_login import UserMixin 
from rssbuddy import login_manager


class Records(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    Party = db.Column(db.String(length = 255), nullable=False)
    Date = db.Column(db.Date(), nullable=False)
    VehicleNo = db.Column(db.String(length = 255))
    Volume = db.Column(db.Float(), nullable=False)
    Rate = db.Column(db.Float(), nullable=False)
    Product = db.Column(db.String(length = 255), nullable=False)
    Amount = db.Column(db.Float(), nullable=False)

    def __repr__(self):
         return f'Date -> {self.Date} | Vehicle No -> {self.VehicleNo}'

#     @classmethod 
#     def instantiate_from_csv(cls):
#         from datetime import datetime
#         with open('items.csv','r') as f:
#               reader = csv.DictReader(f)
#               items = list(reader)
              
#         for item in items:
             
#              temp_rec = Records(Party = item.get('party'),
#                      Date = datetime.strptime(item.get('date'), '%Y-%m-%d').date(),
#                      VehicleNo = item.get('vehicleno'),                   
#                      Volume = item.get('volume'),
#                      Rate = item.get('rate'),
#                      Product = item.get('product'),
#                      Amount = item.get('amount'))
             
#              db.session.add(temp_rec)
#              db.session.commit()  

         

class party_record(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length = 255))

class AmountRecord(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    AmtDate = db.Column(db.Date(), nullable=False)
    Amount = db.Column(db.Float(), nullable=False)
    AmtParty = db.Column(db.String(length = 255), nullable=False)

#     @classmethod
#     def instantiate(cls):
#          from datetime import datetime
#          with open('items.csv','r') as f:
#               reader = csv.DictReader(f)
#               items = list(reader)
#          for item in items:
#               temp_rec = AmountRecord(AmtDate = datetime.strptime(item.get('date'), '%Y-%m-%d').date(),
#                      Amount = item.get('amount'),                   
#                      AmtParty = item.get('party'))
              
#               db.session.add(temp_rec)
#               db.session.commit() 
               

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))


class User(db.Model , UserMixin):
     id = db.Column(db.Integer(), primary_key = True)
     username = db.Column(db.String(length = 255), nullable= False)
     password_hash = db.Column(db.String(length=255), nullable = False)

     @property
     def password(self):
          return self.password
     
     @password.setter
     def password (self , plain_text):
          self.password_hash = bcrypt.generate_password_hash(plain_text).decode('utf-8')

     def check_password_correction(self,try_password):
          return bcrypt.check_password_hash(self.password_hash,try_password)

     def __repr__(self):
          return f'{self.username} ID -> {self.id}'

class Transactions(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.Date(), nullable=False)
    AccType = db.Column(db.String(length = 255))
    TransType = db.Column(db.String(length = 255))
    Remarks = db.Column(db.String(length = 255))
    Amount = db.Column(db.Float(), nullable=False)


