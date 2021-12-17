from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app = Flask(__name__)
user = getenv('MYSQL_USER') 
pwd = getenv('MYSQL_ROOT_PASSWORD')
host = 'electrical:3306'
dbname = getenv('MYSQL_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+str(user)+":"+str(pwd)+"@"+str(host)+"/"+str(dbname)
app.config.from_pyfile('config.cfg')
app.config['SECRET_KEY'] = str(getenv('MYSQL_SK'))
electrical = SQLAlchemy(app)

import blog.routes
import blog.models

