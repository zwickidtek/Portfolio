from contains import db
from datetime import datetime

tagTypes = ['Project', 'Web-Dev', 'Startup', 'Python', 'JavaScript', 'Career', 'React', 'Auto']

class Articlez(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now())
    text = db.Column(db.String(240), nullable=False)
    tag1 = db.Column(db.String(12), default="Project")
    tag2 = db.Column(db.String(12), default="Startup")
    tag3 = db.Column(db.String(12), default="Career")
    anchor = db.Column(db.String(340))
