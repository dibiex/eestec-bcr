from flask import Flask, request, redirect, url_for, render_template, jsonify
app = Flask(__name__)


a = ["Andrei", "Ioana", "Adelin"]

@app.route('/', methods=['GET'])
def get():
    return render_template("tables.html", users=a)
@app.route('/login', methods=['GET'])
def login():
	return render_template("login.html")