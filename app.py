from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello, World!'

@app.route('/contatti')
def contatti():
    return 'contattaci'
