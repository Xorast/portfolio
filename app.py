
from flask import Flask, render_template
import os
from os import path
if path.exists("env.py"):
  import venv 
SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')


APP = Flask(__name__)

@APP.route('/')
def hello_world():
    return render_template('pages/index.html')

