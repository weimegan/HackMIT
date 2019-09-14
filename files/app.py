#!/usr/bin/env python
from flask import Flask, render_template, request, Response
from test import transform

app = Flask(__name__)


# Serve index template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trans', methods=['POST'])
def trans():
    # data = request.get_json(force=True)
    data = request
    # print(request)
    transform(data)
    return "data"
    

if __name__ == '__main__':
    # Run app
    app.run()
