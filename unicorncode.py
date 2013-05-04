import os
from flask import Flask, render_template, redirect, url_for
from flask import request
from parser import parse


app = Flask(__name__)

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/")
# def index():
# 	return "this is unicorncode"

def hello():
	return render_template("home.html")
    # return """
    # <html>

    # <div id="main">
    #     Type some code.  Press ctrl+enter to run it.<hr>
    #     <textarea id="repl" name="code" rows="25" cols="80" ></textarea>
    # </div>
    # </html>


    # """

@app.route('/parse')
def route():
    return '<pre>' + parse(request.args.get('lines', '')) + '</pre>'


if __name__ == "__main__":
	app.run(debug=True)