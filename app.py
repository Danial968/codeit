import os
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.after_request
def apply_content_type(response):
    response.headers["Content-type"] = "application/json"
    return response

@app.route('/chessgame', methods = ["POST"])
def aus():
    test = requests.json
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

    right = True
    left = True
    up = True
    down = True

    diag_left_down = True
    diag_right_down = True
    diag_right_up = True
    diag_left_up = True

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
            if(obs[1] > queen[1] and right):
                steps_right = obs[1] - queen[1]
                right = False
            elif(left):
                steps_left = queen[1] - obs[1]
                left = False
        
        if obs[1] == queen[1]:
            if obs[0] > queen[0] and down:
                steps_down = obs[0] - queen[0] - 1
                down = False
            elif(up):
                steps_up = queen[0] - obs[0] - 1
                up = False

        if(queen_diagonal_right != obs and queen_diagonal_right[1] <= n and diag_right_down):
            diagonal_right += 1
            diag_right_down = False

        if(queen_diagonal_left != obs and queen_diagonal_left[1] > 0 and diag_left_down):
            diagonal_left += 1
            diag_left_down = False

        if(queen_diagonal_right_up != obs and queen_diagonal_right_up[0] > 0 and diag_right_up):
            diagonal_right_up += 1
            diag_left_up = False
        
        if(queen_diagonal_left_up != obs and queen_diagonal_left_up[0] > 0 and queen_diagonal_left_up[1] > 0 and diag_left_up):
            diagonal_left_up += 1
            diag_left_up = False

    total = diagonal_left + diagonal_left_up + diagonal_right + diagonal_right_up + steps_down + steps_left + steps_right + steps_up


    return jsonify(total)





    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))



