from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/web-app-python.herokuapp.com/')
def hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run()
