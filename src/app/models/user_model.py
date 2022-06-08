from app.utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    body_email = db.Column(db.String(100), unique=True)
    domain_email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    password = db.Column(db.String(100))


    def __init__(self, name, lastName, bodyEmail, domainEmail, phone, password):
        self.name = name
        self.last_name = lastName
        self.body_email = bodyEmail
        self.domain_email = domainEmail
        self.phone = phone
        self.password = password