import os
from flask import Flask, jsonify, request
import random

app = Flask(__name__)
@app.after_request
def apply_content_type(response):
    response.headers["Content-type"] = "application/json"
    return response




    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))



