from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html');

@app.route('/stegimg')
def stegimg():
    return render_template('stegimg.html');

@app.route('/stegaud')
def stegaud():
    return render_template('stegaud.html');

@app.route('/flag')
def flag():
    return render_template('encryption.html');


@app.route('/cat/form')
def ping_form():
    return render_template('cat.html');


@app.route('/cat/output', methods = ['POST', 'GET'])
def ping():
    if request.method == 'POST':
        stock = request.form['stock']
        msg = os.popen('cat stocks/' + stock).read()
        return render_template('msg.html', msg=msg) 

