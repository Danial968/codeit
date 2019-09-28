import os
from flask import Flask, jsonify, request

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

@app.route('/sort', methods = ["POST"])
def aus():
    def countsort(x):
        m = max(x)
        buckets = [0] * (m+1)
        for a in x: buckets[a] += 1
        
        return [ b for c in ( [a] * buckets[a] for a in range(m+1) ) for b in c ]
    input = request.json
    return jsonify(countsort(input))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

