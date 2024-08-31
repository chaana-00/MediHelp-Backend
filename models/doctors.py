from app import db


class Doctors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hospital = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    specifications = db.Column(db.String(200), nullable=False)
