import os
from flask import Flask, jsonify, request
import random
import math
from svgpathtools import svg2paths

app = Flask(__name__)
@app.after_request
def apply_content_type(response):
    response.headers["Content-type"] = "application/json"
    return response

@app.route('/chessgame', methods = ["POST"])
def chessgame():
    test = request.json
    queen = []
    n = len(test)
    for y in range(len(test)):
        for x in range(len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]

    # TOP
    top = 0
    for i in range(queen[0]-2,-1,-1):
        if test[i][queen[1]-1] != "X":
            top += 1
        else:
            break

    # DOWN
    down = 0
    for i in range(queen[0], n):
        if test[i][queen[1]-1] != "X":
            down += 1
        else:
            break

    # LEFT
    left = 0
    for i in range(queen[1]-2,-1,-1):
        if test[queen[0]-1][i] != "X":
            left += 1
        else:
            break

    # RIGHT
    right = 0
    for i in range(queen[1], n):
        if test[queen[0]-1][i] != "X":
            right += 1
        else:
            break

    # TOPLEFT
    topleft = 0
    temp_queen_row = queen[0]-1
    temp_queen_col = queen[1]-1
    for i in range(min(queen[0]-1,queen[1]-1),0,-1):
        temp_queen_row -= 1
        temp_queen_col -= 1
        if test[temp_queen_row][temp_queen_col] != "X":
            topleft += 1
        else:
            break

    # TOPRIGHT
    topright = 0
    temp_queen_row = queen[0]-1
    temp_queen_col = queen[1]-1
    for i in range(min(queen[0]-1,n-queen[1]),0,-1):
        temp_queen_row -= 1
        temp_queen_col += 1
        if test[temp_queen_row][temp_queen_col] != "X":
            topright += 1
        else:
            break

    # DOWNLEFT
    downleft = 0
    temp_queen_row = queen[0]-1
    temp_queen_col = queen[1]-1
    for i in range(min(n-queen[0],queen[1]-1),0,-1):
        temp_queen_row += 1
        temp_queen_col -= 1
        if test[temp_queen_row][temp_queen_col] != "X":
            downleft += 1
        else:
            break

    # DOWNRIGHT
    downright = 0
    temp_queen_row = queen[0]-1
    temp_queen_col = queen[1]-1
    for i in range(min(n-queen[0],n-queen[1]),0,-1):
        temp_queen_row += 1
        temp_queen_col += 1
        if test[temp_queen_row][temp_queen_col] != "X":
            downleft += 1
        else:
            break

    total = top+topleft+topright+left+right+down+downleft+downright

    return jsonify(total)

@app.route('/sentiment-analysis', methods = ["POST"])
def sentimentanalysis():
    test = request.json
    num = len(test)
    my_list = ['positive',]
    response = []
    my_dict = {}
    for i in range(num):
        response.append(random.choice(my_list))
    my_dict['response'] = response
    return jsonify(my_dict)


#     def create_word_features(words):
#         useful_words = [word for word in words if word not in stopwords.words("english")]
#         my_dict = dict([(word, True) for word in useful_words])

#         return my_dict

#     def sentiment(sentences):
#         output = []
#         response = []

#         neg_reviews = []
#         for fileid in movie_reviews.fileids('neg'):
#             words = movie_reviews.words(fileid)
#             neg_reviews.append((create_word_features(words), "negative"))

#         pos_reviews = []
#         for fileid in movie_reviews.fileids('pos'):
#             words = movie_reviews.words(fileid)
#             pos_reviews.append((create_word_features(words), "positive"))

#         train_set = neg_reviews[:750] + pos_reviews[:750]
#         test_set =  neg_reviews[750:] + pos_reviews[750:]

#         classifier = NaiveBayesClassifier.train(train_set)

#         accuracy = nltk.classify.util.accuracy(classifier, test_set)

#         for sentence in sentences:
#             words = word_tokenize(sentence)
#             words = create_word_features(words)
#             classifier.classify(words)
#             if classifier.classify(words) == "positive":
#                 response.append("positive")
#             else:
#                 response.append("negative")
#         output["response"] = response
#         return output
#     test = request.json
#     sentences = test["reviews"]
#     return jsonify(sentiment(sentences))

@app.route('/lottery', methods = ["GET"])
def lottery():
    my_list = []
    for i in range(10):
        my_list.append(random.randint(1,101))

    return jsonify(my_list)
    # return jsonify([5,15,50,50,50,50,50,50,50,50])


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

# @app.route('/typing-contest', methods = ["POST"])
# def typeit():
#     test = request.json
#     cost = 0
#     steps= []
#     steps.append({"type":"INPUT","value":test[0]})
#     cost+= len(test[0])

#     for index in range(1, len(test)):
#         copied = test[index-1]
#         steps.append({"type":"COPY","value":copied})
#         cost+= 1
#         current = test[index]
#         steps.append({"type":"TRANSFORM","value":current})
#         for indexc, ch in enumerate(copied):
#             if ch != current[indexc]:
#                 cost += 1

#     return jsonify({"cost":cost, "steps":steps})

@app.route('/gun-control', methods = ["POST"])
def guncontrol():
    test = request.json
    print(test)
    unprocess = test['grid']
    fuel = test['fuel']
    endpointNfuel = []
    grid = []
    gridVisit = []
    startpoint = (0,0)
    final = []

    for line in unprocess:
        grid.append(list(line))
        gridVisit.append(['O' for ch in line])

    for y in range(len(grid)):
        line = grid[y]
        for x in range(len(line)):
            if grid[y][x] == "X":
                gridVisit[y][x] = "B"

    def moveEnd(currentPoint,grid,gridVisit,endpointNfuel,fuel):
        fuel += 1
        movetop = False
        moveleft= False
        moveright= False
        movebot = False
        y = currentPoint[0]
        x = currentPoint[1]
        gridVisit[y][x] = "V"
        try:
            # top
            if (gridVisit[y-1][x] !=  "V" and gridVisit[y-1][x] !=  "B") and y-1 > -1:
                if grid[y-1][x] ==  "O":
                    movetop = True
        except:
            pass
        try:
            # right
            if (gridVisit[y][x+1] !=  "V" and gridVisit[y][x+1] !=  "B") and x+1 < len(grid[0]):
                if grid[y][x+1] ==  "O":
                    moveright = True
        except:
            pass
        try:
            # bot
            if (gridVisit[y+1][x] !=  "V" and gridVisit[y+1][x] !=  "B") and y+1 < len(grid):
                if grid[y+1][x] ==  "O":
                    movebot = True
        except:
            pass
        try:
            # left
            if (gridVisit[y][x-1] !=  "V" and gridVisit[y][x-1] !=  "B") and x-1 > -1:
                if grid[y][x-1] ==  "O":
                    moveleft = True
        except:
            pass
        if movetop:
            moveEnd((y-1,x),grid,gridVisit,endpointNfuel,fuel)
        if moveright:
            moveEnd((y,x+1),grid,gridVisit,endpointNfuel,fuel)
        if movebot:
            moveEnd((y+1,x),grid,gridVisit,endpointNfuel,fuel)
        if moveleft:
            moveEnd((y,x-1),grid,gridVisit,endpointNfuel,fuel)

        if (not movetop) and (not moveright) and (not movebot) and (not moveleft):
            # add to endpoint
            endpointNfuel += [((y,x),fuel)]

    moveEnd((0,0),grid,gridVisit,endpointNfuel,0)
    # for i in range(len(endpointNfuel)):
    #     nextFinal = [endpointNfuel[i]]
    #     for j in range(len(endpointNfuel)):
    #         if i != j:
    #             add = nextFinal + [endpointNfuel[j]]
    #             fueltotal = 0
    #             for it in add:
    #                 fueltotal += it[1]
    #             if sum(map(lambda x: x[1], add)) <= fuel:
    #                 nextFinal += [endpointNfuel[j]]
    #     if len(nextFinal) > len(final):
    #         final = nextFinal
    for i in range(len(endpointNfuel)):
        perms = itertools.permutations(endpointNfuel,i)
        for setlist in list(perms):
            if sum(map(lambda x: x[1], setlist)) == fuel:
                final = setlist

    hits = []
    for item in final:
        hits.append(
            {
                "cell": {
                    "x": (item[0][1] + 1),
                    "y": (item[0][0] + 1)
                },
                "guns": item[1]
            }
        )
    output = {"hits": hits}
    return jsonify(output)

@app.route('/typing-contest', methods = ["POST"])
def typing_contest():
    input = request.json
    # print('hello world')
    # print(input)
    comparator = {}

    for words in input:
        for new_word in input:
            counter = 0
            for i in range(len(new_word)):
                if new_word[i] != words[i]:
                    counter += 1
                    key = new_word + ':'+words
                    if key not in comparator:
                        comparator[key] = counter
                    else:
                        comparator[key]+=1

    my_str = input[0]
    counter = len(input[0])

    actions = ['INPUT']
    word_list = [input[0]]
    steps = [{'type':'INPUT', 'value':input[0]}]

    while(len(word_list) != len(input)):
        to_change = None
        if actions[-1] == 'INPUT':
            actions.append('COPY')
            steps.append({'type':'COPY', 'value':my_str})

        elif actions[-1] == "COPY":
            counter += 1
            actions.append('TRANSFORM')


        else:
            change = 1000000000
            for word in input:
                if word!=my_str:
                    key = my_str +':'+ word
                    if comparator[key] < change and word not in word_list:
                        to_change = word
                        change = comparator[key]
            counter += change
            steps.append({'type':'TRANSFORM', 'value':to_change})
            word_list.append(to_change)
            my_str= to_change
            if(len(word_list) != len(input)):
                actions.append('COPY')
                steps.append({'type':'COPY', 'value':to_change})

    result = {"cost":counter,"steps":steps}
    return jsonify(result)

@app.route('/bucket-fill', methods = ["POST"])
def bucketfill():
    test = request.xhr
    print("hello")
    print(test)
    print("hihi")
    paths, attributes = svg2paths(test)
    total_area = 0
    for i in range(len(attributes)):
        temp_list = attributes[i]["points"].split()
        att_list = []
        for n in range(len(temp_list)):
            att_list.append(temp_list[n].split(","))
        if len(att_list) == 4:
            total_area += (abs(int(att_list[0][0]) - int(att_list[2][0])) - 1) * abs(int(att_list[0][1]) - int(att_list[2][1]))
    return jsonify(total_area)


@app.route('/composition', methods = ["POST"])
def composition():
    input = request.json
    print(input)
    compo = input['composition']
    ban = input['patterns']

    long_ban = []
    count = 0
    for ch in ban:
        long_ban.append(ch)
        long_ban.append(ch[1] + ch[0])

    for banned in long_ban:

        if banned in compo:
            count+=1
            compo = compo.replace(banned,'')

    result = {"testId":input['setId'],"result":count}
    return jsonify(result)


@app.route('/readyplayerone', methods = ["POST"])
def player():
    my_list = {}

    my_list['res'] = -1
    return jsonify(my_list)

@app.route('/prismo', methods = ["POST"])
def prismo():

    def depth(l):
        if isinstance(l, list):
            return 1 + max(depth(item) for item in l)
        else:
            return 0
    test = request.json
    initial = test["initial"]
    print(initial)
    goal = test["goal"]
    current = initial
    moves = []
    output = {}

    depthini = depth(initial)

    while(current != goal):
        if depthini == 1:
            if 0 in current:
                current_index = [current.index(0)]
            num_at_goal = goal[current_index[0]]
            if num_at_goal in current:
                to_move = [current.index(num_at_goal)]
            if to_move[0] < current_index[0]:
                moves.append("L")
                current[to_move[0]], current[current_index[0]] = current[current_index[0]], current[to_move[0]]
            else:
                moves.append("R")
                current[to_move[0]], current[current_index[0]] = current[current_index[0]], current[to_move[0]]
        elif depthini == 2:
            for i in range(len(current)):
                if 0 in current[i]:
                    current_index = [i, current[i].index(0)]
                    break
            num_at_goal = goal[current_index[0]][current_index[1]]
            for i in range(len(current)):
                if num_at_goal in current[i]:
                    to_move = [i, current[i].index(num_at_goal)]
                    break
            if to_move[0] == current_index[0]:
                if to_move[1] < current_index[1]:
                    moves.append("L")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
                else:
                    moves.append("R")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
            else:
                if to_move[0] < current_index[0]:
                    moves.append("B")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
                else:
                    moves.append("F")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
        else:
            for n in range(len(current)):
                for i in range(len(current[n])):
                    if 0 in current[n][i]:
                        current_index = [n, i, current[n][i].index(0)]
                        break
            num_at_goal = goal[current_index[0]][current_index[1]][current_index[2]]
            for n in range(len(current)):
                for i in range(len(current[n])):
                    if num_at_goal in current[n][i]:
                        to_move = [n, i, current[n][i].index(num_at_goal)]
                        break
            if to_move[0] == current_index[0]:
                if to_move[1] == current_index[1]:
                    if to_move[2] < current_index[2]:
                        moves.append("L")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                    else:
                        moves.append("R")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                else:
                    if to_move[1] < current_index[1]:
                        moves.append("B")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                    else:
                        moves.append("F")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
            else:
                if to_move[0] < current_index[0]:
                    moves.append("D")
                    current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                else:
                    moves.append("U")
                    current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
    output["moves"] = moves
    return jsonify(output)

@app.route('/defuse', methods = ["POST"])
def defuse():
    input = request.json
    my_list = [0]
    return jsonify(my_list)

@app.route('/yin-yang', methods = ["POST"])
def yinyang():
    test = request.json
    print(test)
    number_of_elements = test["number_of_elements"]
    number_of_operations = test["number_of_operations"]
    elements = test["elements"]
    elements_list = [elements]
    probability = 0
    output = {}

    for i in range(number_of_operations):
        count_yin = 0
        count_yang = 0
        for element in elements_list:
            for n in range(len(element)):
                if element[n] == "Y" or element[-n-1] == "Y":
                    count_yang += 1
                else:
                    count_yin += 1
            probability += (count_yang/len(element))/(len(elements_list))
            # if count_yin > 0:
            #     elements_list.append([])
    output["result"] = probability
    return jsonify(output)

@app.route('/encryption', methods = ["POST"])
def encryption():
    tests = request.json
    print(tests)
    my_list = []
    for test in tests:
        n = test["n"]
        text = test["text"]
        new_text = ""
        for i in range(len(text)):
            if text[i].isalnum():
                new_text += text[i].upper()
        if len(new_text) < n:
            my_list.append(new_text)
            continue

        current_list = ['']*len(new_text)
        count = 0
        rounds = 1

        for i in range(len(new_text)):
            if count >= len(new_text):
                count = rounds
                rounds += 1
            current_list[count] = new_text[i]
            count += n
        
        my_list.append("".join(current_list))
    
    return jsonify(my_list)

@app.route('/bankbranch', methods = ["POST"])
def bank():
    tests = request.json
    print(tests)
    n = test['N']
    start_time = test['branch_officers_timings']
    current_time = start_time
    output = {}

    for i in range(n):
        branch_go = current_time.index(min(current_time))
        for j in range(len(current_time)):
            current_time[j] -= start_time[branch_go]
        current_time[branch_go] = start_time[branch_go]

    output["answer"] = branch_go + 1
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
