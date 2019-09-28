import os
from flask import Flask, jsonify, request
import random
import math
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
    
    print(test)
    steps_right = n - queen[1]
    steps_left = queen[1] -1



    steps_up = queen[0] - 1
    steps_down = n - queen[0]


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
        else:
            diag_right_down = False
        

        if(queen_diagonal_left != obs and queen_diagonal_left[1] > 0 and diag_left_down):
            diagonal_left += 1
        else:
            diag_left_down = False

        if(queen_diagonal_right_up != obs and queen_diagonal_right_up[0] > 0 and diag_right_up):
            diagonal_right_up += 1

        else:
            diag_left_up = False
        
        if(queen_diagonal_left_up != obs and queen_diagonal_left_up[0] > 0 and queen_diagonal_left_up[1] > 0 and diag_left_up):
            diagonal_left_up += 1

        else:
            diag_left_up = False


    total = diagonal_left + diagonal_left_up + diagonal_right + diagonal_right_up + steps_down + steps_left + steps_right + steps_up


    return jsonify(total)

@app.route('/sentiment-analysis', methods = ["POST"])
def sentimentanalysis():
    test = request.json
    sentences = test["reviews"]
    response = []
    output = {}

    for sentence in sentences:
        sid = SentimentIntensityAnalyzer()
        print(sid.polarity_scores(sentence))
        if sid.polarity_scores(sentence)["neg"] < sid.polarity_scores(sentence)["pos"]:
            response.append("positive")
        else:
            response.append("negative")
    output["response"] = response
    return output

@app.route('/lottery', methods = ["GET"])
def lottery():
    my_list = []
    for i in range(10):
        my_list.append(random.randint(1,101))

    return jsonify(my_list)


@app.route('/maximise_1c', methods = ["POST"])
def maximise1c():
    test = request.json
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
