from flask import render_template, request, redirect, url_for
from datetime import datetime
from UsersDB import app, sqldb
from models import User, Note, LogCount

# Add user
@app.route('/add', methods=['POST'])
def add():
	new_user = User(name = request.form['name'], password = request.form['password'])

	new_note = Note(date = datetime.utcnow(), comment = "User " + new_user.name + " was added.")
	LogCount.added = LogCount.added + 1
	LogCount.save()

	sqldb.session.add(new_user)
	sqldb.session.commit()
	new_note.save()
	return redirect(url_for('index'))

# Delete user
@app.route('/delete', methods=['POST'])
def delete():
	to_delete_id = request.form['del_id']
	to_delete = User.query.filter_by(id = to_delete_id).first()

	new_note = Note(date = datetime.utcnow(), comment = "User " + to_delete.name + " was deleted.")
	LogCount.deleted = LogCount.deleted + 1
	LogCount.save()

	sqldb.session.delete(to_delete)
	sqldb.session.commit()
	new_note.save()
	return redirect(url_for('index'))

# Edite user
@app.route('/update', methods=['POST'])
def update():
	to_update_id = request.form['upd_id']
	to_update = User.query.filter_by(id = to_update_id).first()
	old_username = to_update.name
	to_update.name = request.form['upd_name']
	to_update.password = request.form['upd_comment']

	if old_username == to_update.name:
		new_note = Note(date = datetime.utcnow(), comment = "Users " + old_username + " password was updated")
	else:
		new_note = Note(date = datetime.utcnow(), comment = "User " + old_username + " was updated to " + to_update.name)
	LogCount.edited = LogCount.edited + 1
	LogCount.save()

	sqldb.session.commit()
	new_note.save()
	return redirect(url_for('index'))

# @app.route('/reset_id', methods=['POST'])
# def reset_id():
# 	return redirect(url_for('index'))
