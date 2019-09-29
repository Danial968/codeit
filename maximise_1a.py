import itertools
import pandas as pd
def maximise_1a(test):

    startingCapital = test["startingCapital"]
    stocks = test["stocks"]
    output = {}
    best_stock = []
    profit = 0
    portfolio = []

    for stock in itertools.permutations(stocks):
        tempCapital = startingCapital
        count = 0
        tempfolio = {}
        tempfolio['profit'] = 0
        tempfolio['portfolio'] = []


        read = stock[count][2]

        while(tempCapital != 0 and stock[count][2] <= tempCapital and stock[count][0] not in tempfolio['portfolio']):
            tempCapital -= stock[count][2]
            
            tempfolio['profit'] += stock[count][1]
            tempfolio['portfolio'].append(stock[count][0])
            count +=1
            if count > len(stock):
                count = 0

        if tempCapital < 0:
            tempfolio['portfolio'].pop()
            tempfolio['profit'] -= stock[count][1]

        portfolio.append(tempfolio)
    # print(type(portfolio))
    # print(pd.DataFrame(portfolio))

    highest = 0

    for my_dict in portfolio:
        if my_dict['profit'] > highest:
            highest = my_dict['profit']
            answer = my_dict

    print(answer)
json = {
        "startingCapital": 400,
        "stocks": [
            [
                "Sony",
                30, 
                400 
            ],
            [
                "Dell",
                20,
                300
            ],
            [
                "Disney",
                15,
                100
            ],
            [
                "Apple",
                20,
                100
            ]
        ]
    }

(maximise_1a(json))