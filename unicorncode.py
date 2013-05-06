import os
from flask import Flask, render_template, redirect, url_for, session, flash, g
from flask import request
from parser import parse
import model
import markdown
from model import session as db_session, User, Tutorial
from forms import TutorialForm


app = Flask(__name__)

# @app.route("/home")
# def home():
# 	return render_template("home.html")

@app.teardown_request
def shutdown_session(exception = None):
    db_session.remove()

@app.before_request
def load_user_id():
    g.user_id = session.get('user_id')


@app.route("/")
@app.route("/index")
def index():
	tutorials = db_session.query(Tutorial).all()
	return render_template("home.html", tutorials=tutorials)

@app.route('/parse')
def route():
    return '<pre>' + parse(request.args.get('lines', '')) + '</pre>'

@app.route("/try_tutorial/<int:id>", methods=["GET"])
def try_tutorial(id):
	tutorials = db_session.query(Tutorial).all()
	tutorial = db_session.query(Tutorial).get(id)
	rendered_tutorial = markdown.markdown(tutorial.tutorial, safe_mode='escape')
	return render_template("try_tutorial.html", tutorial=rendered_tutorial, tutorials=tutorials)


@app.route("/tutorials")
def list_tutorials():
	if not g.user_id:
		return redirect(url_for("index"))
	tutorials = db_session.query(Tutorial).all()
	return render_template("list_tutorials.html", tutorials=tutorials)

@app.route("/tutorial/<int:id>", methods=["GET"])
def view_tutorial(id):
	if not g.user_id:
		return redirect(url_for("index"))
	tutorial = db_session.query(Tutorial).get(id)
	rendered_tutorial = markdown.markdown(tutorial.tutorial, safe_mode='escape')
	return render_template("tutorial.html", tutorial=tutorial, tutorial_text=rendered_tutorial)

@app.route("/tutorials/new_tutorial", methods=["GET", "POST"])
def new_tutorial():
	if not g.user_id:
		return redirect(url_for("index"))

	form = TutorialForm(request.form)
	if request.method == 'POST' and form.validate():
		title = form.title.data
		tutorial = form.tutorial.data
		new_tutorial = Tutorial(title=title, tutorial=tutorial)
		db_session.add(new_tutorial)
		db_session.commit()
		return redirect(url_for("list_tutorials"))
	return render_template('new_tutorial.html', form=form)

@app.route("/tutorials/delete_tutorial/<int:id>", methods=["GET"])
def delete_tutorial(id):
	if not g.user_id:
		return redirect(url_for("index"))
	tutorial = db_session.query(Tutorial).get(id)
	db_session.delete(tutorial)
	db_session.commit()
	return redirect(url_for("list_tutorials"))


@app.route("/tutorials/edit_tutorial/<int:id>", methods=['GET', 'POST'])
def edit_tutorial(id):
	if not g.user_id:
		return redirect(url_for("index"))
	tutorial = db_session.query(Tutorial).get(id)
	form = TutorialForm(request.form, tutorial)

	if request.method == "POST" and form.validate():
		tutorial.title = form.title.data
		tutorial.tutorial = form.tutorial.data
		db_session.add(tutorial)
		db_session.commit()
		return redirect(url_for("list_tutorials"))

	rendered_tutorial = markdown.markdown(tutorial.tutorial, safe_mode='escape')
	return render_template('tutorial.html', form=form, tutorial=tutorial, tutorial_text=rendered_tutorial)

@app.route('/admin')
def login():
    return render_template("login.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
	email = request.form['email']
	password = request.form['password']
	user = db_session.query(User).filter_by(email=email, password=password).one()
	session['user_id'] = user.id
	return redirect(url_for("list_tutorials"))

@app.route("/logout")
def logout():
    del session['user_id']
    return redirect(url_for("login"))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
   
if __name__ == "__main__":
	app.run(debug=True)