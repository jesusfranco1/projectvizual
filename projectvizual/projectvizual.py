#Jesus Franco
from flask import Flask, request, render_template
from flask_pymongo import PyMongo
import json

'''connecting to mongodb using PyMongo. the database name is passed in
    as a flask argument'''
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
