from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///guidesNblogs.sqlite"
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/guide/<id>')
def guide(id):
    return render_template('guide.html', guide=id)


db.create_all()
app.run(debug=True)
