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
    test = request.json
    queen = []
    obstacles = []
    print(test)
    for y in range(len(test)):
        n = len(test)

        for x in range(len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]
            if test[y][x] == 'X':
                obstacles.append([y+1,x+1])
    
    steps_right = n- queen[1]
    steps_left = queen[1]-1
    
    steps_up = queen[0] - 1
    steps_down = n- queen[0]
    queen_diagonal_right = queen.copy()
    diagonal_right = 0 
    diagonal_left = 0

    diagonal_right_up = 0
    diagonal_left_up = 0

    queen_diagonal_left = queen.copy()

    queen_diagonal_left_up = queen.copy()
    queen_diagonal_right_up = queen.copy()

    for obs in obstacles:
        queen_diagonal_right[0] += 1
        queen_diagonal_right[1] += 1

        queen_diagonal_left[0] += 1
        queen_diagonal_left[1] -= 1

        queen_diagonal_right_up[0] -= 1
        queen_diagonal_right_up[1] += 1

        queen_diagonal_left_up[0] -= 1
        queen_diagonal_left_up[1] -= 1

        if obs[0] == queen[0]:
            if(obs[1] > queen[1]):
                steps_right = obs[1] - queen[1]
            else:
                steps_left = queen[1] - obs[1]
        
        if obs[1] == queen[1]:
            if obs[0] > queen[0]:
                steps_down = obs[0] - queen[0] - 1
            else:
                steps_up = queen[0] - obs[0] - 1

        if(queen_diagonal_right != obs and queen_diagonal_right[1] <= n):
            diagonal_right += 1

        if(queen_diagonal_left != obs and queen_diagonal_left[1] > 0 ):
            diagonal_left += 1

        if(queen_diagonal_right_up != obs and queen_diagonal_right_up[0] > 0):
            diagonal_right_up += 1
        
        if(queen_diagonal_left_up != obs and queen_diagonal_left_up[0] > 0 and queen_diagonal_left_up[1] > 0):
            diagonal_left_up += 1

        
    total = diagonal_left + diagonal_left_up + diagonal_right + diagonal_right_up + steps_down + steps_left + steps_right + steps_up

    
    return jsonify(total)

@app.route('/lottery', methods = ["POST"])
def aus():
    input = request.json
    my_list = []
    for x in range(10):
        my_list.append(random.randint(1,101))
    return jsonify(my_list)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))



