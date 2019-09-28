import os
from flask import Flask, jsonify, request
import random

app = Flask(__name__)
@app.after_request
def apply_content_type(response):
    response.headers["Content-type"] = "application/json"
    return response

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/square', methods=['POST'])
def square():
    req = request.json
    number = int(req['input']) ** 2
    return f"{number}"

@app.route('/chessgame', methods = ["POST"])
def aus():
    input = request.json
    input.sort()
    return jsonify(input)

@app.route('/lottery', methods = ["POST"])
def aus():
    input = request.json
    my_list = []
    for x in range(10):
        my_list.append(random.randint(1,101))
    return jsonify(my_list)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))



