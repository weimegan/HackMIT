#!/usr/bin/env python
from flask import Flask, render_template, request, Response
from transcriber import transcriber

app = Flask(__name__)


# Serve index template
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    # Change to whatever path you want to save the recording to
    file_path = "/Users/Amanda/Downloads/audio.mp3"
    file.save(file_path)
    transcriber(file_path)
    return file_path
    

if __name__ == '__main__':
    # Run app
    app.run()
