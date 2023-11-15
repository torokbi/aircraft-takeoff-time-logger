from logger import db

class Planes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registracion = db.Column(db.String, nullable=False)
    takeofftime = db.Column(db.Time, nullable=False)