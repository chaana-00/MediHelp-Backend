from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    nic = db.Column(db.String(100), unique=True)
    age = db.Column(db.String(100))
    gender = db.Colum(db.String(100))
    address = db.Column(db.String(100))
    mobile = db.Column(db.String(100), unique=True)
    img = db.Column(db.String(255))
    password = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
