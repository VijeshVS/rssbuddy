from rssbuddy import db

class SML(db.Model):
    ID = Date = db.Column(db.Integer(), primary_key=True)
    Date = db.Column(db.String(length = 10), nullable=False)
    VehicleNo = db.Column(db.String(length = 20), nullable=False)
    Volume = db.Column(db.Integer(), nullable=False)
    Rate = db.Column(db.Integer(), nullable=False)
    Product = db.Column(db.String(length = 10), nullable=False)
    Amount = db.Column(db.Integer(), nullable=False)



