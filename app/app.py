#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Welocome to my app!<h1>'
    
@app.route('/<username>')
def user(username):
    return f'<h1>profile for {username}</h1> '
if __name__=='__main__':
    app.run(port=5555)