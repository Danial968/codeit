import itertools

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
        while(tempCapital != 0):
            tempCapital -= stock[count]

        # for i in range(len(stock)):


    print(all_stocks)


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

print(maximise_1a(json))