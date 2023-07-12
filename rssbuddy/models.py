from rssbuddy import db

class Records(db.Model):
    Party = Date = db.Column(db.String(length = 10), nullable=False)
    ID = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.Date(), nullable=False)
    VehicleNo = db.Column(db.String(length = 20), nullable=False)
    Volume = db.Column(db.Integer(), nullable=False)
    Rate = db.Column(db.Integer(), nullable=False)
    Product = db.Column(db.String(length = 10), nullable=False)
    Amount = db.Column(db.Integer(), nullable=False)

class party_record(db.Model)   :
    name = db.Column(db.String(length = 10))
    ID = db.Column(db.Integer(), primary_key=True)

class AmountRecord(db.Model):
    ID = db.Column(db.Integer(), primary_key=True)
    AmtDate = db.Column(db.String(length = 10), nullable=False)
    Amount = db.Column(db.Integer(), nullable=False)
    AmtParty =  db.Column(db.String(length = 10), nullable=False)
    


