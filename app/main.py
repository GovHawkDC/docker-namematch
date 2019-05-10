#!flask/bin/python
from flask import Flask, request
from whoswho import who
import json

app = Flask(__name__)
@app.route('/')

def index():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    return str(who.ratio(name1, name2))

if __name__ == '__main__':
    app.run()