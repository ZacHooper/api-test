import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():

    data = {
        "time": [
            {"test":1}
        ]
    }


    return data