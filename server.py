from flask import Flask, request, redirect, url_for, render_template, jsonify
app = Flask(__name__)
import pymysql
import os

app.secret_key = os.urandom(24)

class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "userdb"
        password = "password"
        db = "bcrdb"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def list_users(self):
        self.cur.execute("SELECT id, name, password FROM users LIMIT 50")
        result = self.cur.fetchall()
        return result
    def list_clienti(self):
        self.cur.execute("SELECT id, name, surname, birth, resend FROM clienti LIMIT 50")

@app.route('/', methods=['GET', 'POST'])
def get():
    db =Database()
    result = db.list_users()

    resid = ""
    for res in result:
       resid = res["id"] 
    return " hello"  +" " + str(resid)+" "

a = ["Andrei", "Ioana", "Adelin"]



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #data = request.form['email']
        res = ""
        return str(request.form.get('email'))
    return render_template("login.html")


@app.route('/tables', methods=['GET'])
def tables():
    return render_template("tables.html", users=a)

@app.route('/form', methods=['GET'])
def form():
	return render_template("form.html")