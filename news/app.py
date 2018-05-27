from flask import Flask, render_template
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    path = '/home/shiyanlou/files/'
    files = os.listdir(path)
    json_list = []
    for name in files:
        if 'json' in name:
            json_list.append(name)
    json_all = []
    
    test = {'111':123,'222':345}
    for x in json_list:
        with open(path+x) as file:
            json_all.append(json.loads(file.read()))
    return render_template('index.html', article=json_all, name=json_list,test=test)


@app.route('/files/<filename>')
def file(filename):
    path = '/home/shiyanlou/files/'
    filename = filename + '.json'
    if os.path.exists(path+filename) == False :
        not_found()
    with open(path+filename) as file:
        json_filename = json.loads(file.read())
    return render_template('file.html',json=json_filename)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
        

