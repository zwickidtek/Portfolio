from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
from contains.models import Articlez

# configure database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///guidesNblogs.db"
app.config["SECRET_KEY"] = '289ab84d2d6466f93361c87e'
db.create_all()
# create some test data
# new_article = Articlez(text="Welcome to my page! This is my first article and I am excited by all the space for activities!", tag1="Web-Dev", tag2="Python", tag3="Project")
# db.session.add(new_article)
# db.session.commit()
from contains import routes
