import os
from flask import Flask, jsonify, request
import random

app = Flask(__name__)
@app.after_request
def apply_content_type(response):
    response.headers["Content-type"] = "application/json"
    return response

@app.route('/chessgame', methods = ["POST"])
def aus():
    test = request.json
    queen = []
    obstacles = []

    print(test)




@app.route('/generateSequence', methods = ["POST"])
def aus():

    input = request.json
    modules = input['modules']
    print(modules)  
    dependency = input[dependencyPairs]
    # return jsonify(modules)
    # return(test)
    return '0'



    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))



