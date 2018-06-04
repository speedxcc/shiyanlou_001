from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json
import collections

from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)
mg =client.shiyanlou009


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
        '''
        if data:
        '''
        tags = mg.tags.find_one({'title':self.title})['tag_name']
        if not tag_name in tags:
            tags.append(tag_name)
            mg.tags.update_one({'title':self.title},{'$set':{'tag_name':tags}})
        '''
        else:
            mg.tags.insert_one({'title': self.title, 'tag_name': [tag_name]})
        if tag_name not in tag['tag_name']:
            li = tag['tag_name']
            add_tag = li.append('tag_name')
            mg.tags.update_one({'title':self.title},{'$set':{'tag_name':add_tag}})
        '''

    def remove_tag(self,tag_name):
        tags = mg.tags.find_one({'title':self.title})['tag_name']
        if tag_name in tags:
            tags.remove(tag_name)
            mg.tags.update_one({title:'self.title'},{'$set':{'tag_name': tags}})

    @property
    def tags(self):
        tags = mg.tags.find_one({'title':self.title})['tag_name']
        return tags

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content
        user = {'title': self.title, 'tag_name': [] }
        mg.tags.insert_one(user)
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
    tags = File.tags 
    return render_template('file.html',wenzhang=wenzhang,cate=cate,tags=tags)

    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
        

