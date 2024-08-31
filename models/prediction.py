from app import db

class Prediction(db.Model):
    __tablename__ = 'prediction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    prediction = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, prediction, datetime, age):
        self.user_id = user_id
        self.prediction = prediction
        self.datetime = datetime
        self.age = age
