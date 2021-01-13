import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class contact_form(db.Model):
    __tablename__ = 'forms'
    
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    SQLAlchemy = ''' INSERT INTO Post(id,firstName,lastName,email,message)
              VALUES(?,?,?,?,?) '''

    def __init__(self,firstName,lastName,email,message):
        self.firstName =firstName
        self.lastName =lastName
        self.email=email
        self.message=message


    def __repr__(self):
        return f"form('{self.firstName}','{self.date_posted}')"
