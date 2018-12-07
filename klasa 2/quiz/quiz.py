#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><center>Aplikacja QUIZ</center><h1>"

@app.route("/strona")
def strona():
    return render_template('strona.html')
    
@app.route("/klasa")
def klasa():
    return render_template('klasa.html')

if __name__ == '__main__':
    app.run(debug=True)
