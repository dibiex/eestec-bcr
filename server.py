from flask import Flask, request, redirect, url_for, render_template, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return '''hello'''
