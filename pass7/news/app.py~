from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json
import collections

from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)
mg =client.shiyanlou


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

    def add_tag(self,tag_name):
        user = {'id': self.id, 'tag_name': tag_name }
        number = 'id'+str(self.id)
        mg.number.insert_one(user)
        

    def remove_tag(self,tag_name):
        number = 'id'+str(self.id)
        mg.number.delete_one({tag_name:'tag_name'})
    @property
    def tags(self):
        number = 'id'+str(self.id)
        tags = mg.number.find_one({id:'self.id'})
        return tags

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
    wenzhang = File.query.filter_by(id=file_id).first()
    cate = Category.query.filter_by(id=wenzhang.id).first()
     
    return render_template('file.html',wenzhang=wenzhang,cate=cate)

    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
        

