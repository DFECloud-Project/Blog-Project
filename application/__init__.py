from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app = Flask(__name__)
user = getenv('MYSQL_USER') 
pwd = getenv('MYSQL_PWD')
ip= getenv('MYSQL_IP')
dbname = getenv('MYSQL_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+user+":"+pwd+"@"+ip+"/"+dbname
app.config['SECRET_KEY'] = getenv('MYSQL_SK')
db = SQLAlchemy(app)

import application.routes
import application.models

