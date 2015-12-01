from app import db
from app import app
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    
    def __init__(self,data):
        self.data = data
        self.timestamp = datetime.now()
    def __repr__(self):
        return "<Data %r>" % self.data
