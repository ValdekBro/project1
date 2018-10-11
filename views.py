from flask import render_template, request
from UsersDB import app, sqldb
from models import User, Note, LogCount

@app.route('/', methods=['GET'])
def index():
	users = User.query.all()
	return render_template('index.html', users=users)

# Add user
@app.route('/user_form', methods=['GET'])
def user_form():
	return render_template('add_user.html')

# Edite user
@app.route('/upd_user_form', methods=['GET'])
def upd_user_form():
	upd_id = request.args.get('upd_id')
	return render_template('update_user.html', upd_id=upd_id)

@app.route('/user_log', methods=['GET'])
def user_log():
	notes = Note.query.all()
	return render_template('user_log.html', notes=notes, LogCount=LogCount)
