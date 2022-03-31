from flask_sqlalchemy import model
from contains import db
class Guide(db.model):
    id = db.Column(db.String, 240);
