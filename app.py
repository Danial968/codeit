import os
from flask import Flask, jsonify, request
import random
import math

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
    for y in range(len(test)):
        n = len(test)

        for x in range(len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]
            if test[y][x] == 'X':
                obstacles.append([y+1,x+1])

    queen_row = queen[0]
    queen_col = queen[1]
    
    top = queen_row-1
    down = abs(n-queen_row)
    left = queen_col-1
    right = abs(n-queen_col)
    ttop_right = min(top, right)
    ttop_left = min(top, left)
    tdown_right = min(down, right)
    tdown_left = min(down, left)
    top_right = min(top, right)
    top_left = min(top, left)
    down_right = min(down, right)
    down_left = min(down, left)
    for i in range(len(obstacles)):
        # Left
        if(obstacles[i][0] == queen_row):
            if(obstacles[i][1] < queen_col):
                temp = abs(obstacles[i][1]-queen_col)-1
                if(left > temp):
                    left = temp
            # right
            else:
                temp = abs(obstacles[i][1]-queen_col)-1
                if(right > temp):
                    right = temp
        # Top
        elif(obstacles[i][1] == queen_col):
            if(obstacles[i][0] < queen_row):
                temp = abs(obstacles[i][1]-queen_col)-1
                if(top > temp):
                    top = temp
            # down
            else:
                temp = abs(obstacles[i][0]-queen_row)-1
                if(down > temp):
                    down = temp
    temp_queen = queen
    for i in range(ttop_right):
        temp_queen[0] -= 1
        temp_queen[1] += 1
        if(temp_queen in obstacles):
            index = obstacles.index(temp_queen)
            temp = abs(obstacles[index][0]-queen_row)-1
            if(top_right > temp):
                top_right = temp
    temp_queen = queen
    for i in range(ttop_left):
        temp_queen[0] += 1
        temp_queen[1] += 1
        if(temp_queen in obstacles):
            index = obstacles.index(temp_queen)
            temp = abs(obstacles[i][0]-queen_row)-1
            if(down_left > temp):
                down_left = temp
    temp_queen = queen
    for i in range(tdown_right):
        temp_queen[0] += 1
        temp_queen[1] -= 1
        if(temp_queen in obstacles):
            index = obstacles.index(temp_queen)
            temp = abs(obstacles[i][0]-queen_row)-1
            if(down_right > temp):
                down_right = temp
    temp_queen = queen
    for i in range(tdown_left):
        temp_queen[0] -= 1
        temp_queen[1] -= 1
        if(temp_queen in obstacles):
            index = obstacles.index(temp_queen)
            temp = abs(obstacles[i][0]-queen_row)-1
            if(top_left > temp):
                top_left = temp


    return jsonify(top+top_left+top_right+right+left+down+down_left+down_right)




@app.route('/lottery', methods = ["GET"])
def test():
    my_list = []
    for i in range(10):
        my_list.append(random.randint(1,101))

    return jsonify(my_list)


@app.route('/maximise_1c', methods = ["POST"])
def nic():
    test = request.json
    print(test)
    startingCapital = test["startingCapital"]
    stocks = test["stocks"]
    stocks_value = {}
    sorted_value_stock = []
    output = {}
    profit = 0
    portfolio = [] 

    for i in range(len(stocks)):
        stocks_value[stocks[i][0]] = stocks[i][1]/stocks[i][2]
        sorted_value_stock.append([stocks[i][0], stocks[i][1], stocks[i][2], stocks[i][1]/stocks[i][2]])
    sorted_value_stock.sort(key=lambda x: x[3], reverse=True)
    
    count = 0
    while(startingCapital != 0):
        if startingCapital >= sorted_value_stock[count][2]:
            startingCapital -= sorted_value_stock[count][2]
            profit += sorted_value_stock[count][1]
            portfolio.append(sorted_value_stock[count][0])
        else:
            if(count == len(sorted_value_stock)-1):
                break
            count += 1
    output["profit"] = profit
    output["portfolio"] = portfolio

    return jsonify(output)

@app.route('/generateSequence', methods = ["POST"])
def depend():
    test = request.json
    final = []
    dependency = {}
    stack = set({})
    moduleSet = set(test["modules"])

    for item in test["dependencyPairs"]:
        if item["dependee"] in dependency:
            dependency[item["dependee"]] += [item["dependentOn"]]
        else:
            dependency[item["dependee"]] = [item["dependentOn"]]
        stack.add(item["dependee"])

    # add with no dependentOn
    for item in moduleSet.difference(stack):
        final += [item]
    for item in final:
        moduleSet.remove(item)

    #fff
    prevCount = len(moduleSet)
    currentCount = -1
    
    while currentCount!= prevCount:
        prevCount = len(moduleSet)
        nextF = []
        for item in moduleSet:
            dependsOn = dependency[item]
            if all(elem in final  for elem in dependsOn):
                nextF += [item]
        final += nextF 
        for item in nextF:
            moduleSet.remove(item)
        currentCount = len(moduleSet)
    
    return  jsonify(final)

@app.route('/exponent', methods = ["POST"])
def exponential():
    test = request.json
    n = test["n"]
    p = test["p"]

    def first_digit(n, p):
        if p == 0:
            return 1
        if n == 0:
            return 0
        value = p*(math.log10(n))
        frac, whole = math.modf(value)
        return int(str(10**frac)[:1])

    def len_digit(n, p):
        if n == 0:
            return 1
        if p == 0:
            return 1
        return int(p*(math.log10(n))+1)

    def last_digit(n1, n2):
        if n2 == 0:
            return 1
        if n1 == 0:
            return 0

        cycle = [n1 % 10]
        while True:
            nxt = (cycle[-1] * n1) % 10
            if nxt == cycle[0]:
                break
            cycle.append(nxt)
        return cycle[(n2 - 1) % len(cycle)] 

    my_dict = {}
    my_dict['result'] = [first_digit(n, p), len_digit(n,p), last_digit(n, p)]

    return jsonify(my_dict)

@app.route('/typing-contest', methods = ["POST"])
def typeit():
    test = request.json
    cost = 0
    steps= []
    steps.append({"type":"INPUT","value":test[0]})
    cost+= len(test[0])

    for index in range(1, len(test)):
        copied = test[index-1]
        steps.append({"type":"COPY","value":copied})
        cost+= 1
        current = test[index]
        steps.append({"type":"TRANSFORM","value":current})
        for indexc, ch in enumerate(copied):
            if ch != current[indexc]:
                cost += 1

    return jsonify({"cost":cost, "steps":steps})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
