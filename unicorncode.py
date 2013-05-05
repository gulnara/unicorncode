import os
from flask import Flask, render_template, redirect, url_for
from flask import request
from parser import parse
import model
from model import session as db_session, User, Tutorial



app = Flask(__name__)

# @app.route("/home")
# def home():
# 	return render_template("home.html")

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
   
if __name__ == "__main__":
	app.run(debug=True)