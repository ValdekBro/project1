from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mongoalchemy import MongoAlchemy
from flask_moment import Moment

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://valdek:val135246dek@sql3.db4free.net/valdekdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MONGOALCHEMY_DATABASE'] = 'usersdb'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://valdek:val135246dek@ds121673.mlab.com:21673/usersdb'

moment = Moment(app)
sqldb = SQLAlchemy(app)
nosqldb = MongoAlchemy(app)

from views import *
from controllers import *
from models import User

if __name__ == '__main__':
	app.run(debug=True)
