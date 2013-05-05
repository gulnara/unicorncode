import os
from flask import Flask, render_template, redirect, url_for
from flask import request
from parser import parse
import model
from model import session as db_session, User, Tutorial
from forms import TutorialForm


app = Flask(__name__)

# @app.route("/home")
# def home():
# 	return render_template("home.html")

@app.teardown_request
def shutdown_session(exception = None):
    db_session.remove()

@app.route("/")
@app.route("/index")
def index():
	return render_template("home.html")

@app.route('/parse')
def route():
    return '<pre>' + parse(request.args.get('lines', '')) + '</pre>'

@app.route('/admin')
def login():
    return render_template("login.html")

@app.route("/tutorials")
def list_tutorials():

	tutorials = db_session.query(Tutorial).all()
	return render_template("list_tutorials.html", tutorials=tutorials)

@app.route("/tutorial/<int:id>", methods=["GET"])
def view_tutorial(id):
	tutorial = db_session.query(Tutorial).get(id)
	
	return render_template("tutorial.html", tutorial=tutorial)

@app.route("/new_tutorial", methods=["POST"])
def new_tutorial():

	title = request.form['title']
	tutorial = request.form['text']
	new_tutorial = Tutorial(title=title, tutorial=tutorial)
	db_session.add(new_tutorial)
	db_session.commit()
	return redirect(url_for("list_tutorials"))

@app.route("/tutorials/delete_tutorial/<int:id>", methods=["GET"])
def delete_tutorial(id):
	tutorial = db_session.query(Tutorial).get(id)
	db_session.delete(tutorial)
	db_session.commit()
	return redirect(url_for("list_tutorials"))


@app.route("/tutorials/edit_tutorial/<int:id>", methods=['GET', 'POST'])
def edit_tutorial(id):
	tutorial = db_session.query(Tutorial).get(id)
	form = TutorialForm(request.form)
	if request.method == "POST" and form.validate():
		tutorial.title = form.title.data
		tutorial.tutorial = form.text.data
		db_session.add(tutorial)
		db_session.commit()
		return redirect(url_for("list_tutorials"))
	return render_template('tutorial.html', form=form, tutorial=tutorial)


   
if __name__ == "__main__":
	app.run(debug=True)