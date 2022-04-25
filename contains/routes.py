from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from contains.models import Articlez
from contains import app, db


@app.route('/')
def hello():
    articles = Articlez.query.all()
    return render_template('index.html', notes=articles)


@app.route('/guide/<id>')
def guide(id):
    return render_template('guide.html', guide=id)


@app.route('/b')
def blogs():
    return render_template('blog.html')


db.create_all()
if __name__=="__main__":
    app.run(debug=True, port=3000)
