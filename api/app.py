from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def index():
    data = {
        "test":[
            {"test-1":1},
            {"test-2":2}
        ]
    }
    return jsonify(data)