from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category')
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
    def __repr__(self):
        return '<File(name=%s)>' % self.id

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category(name=%s)>' % self.name

@app.route('/')
def index():
    art = File.query.all()
    return render_template('index.html',art=art)

@app.route('/files/<file_id>')
def file(file_id):
    wenzhang = File.query.filter_by(id='file_id').first()
     
    return render_template('file.html',wenzhang=wenzhang)
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
        

