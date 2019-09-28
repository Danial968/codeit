def maximise_1c(json):
    startingCapital = json["startingCapital"]
    stocks = json["stocks"]
    sorted_value_stock = []
    output = {}
    profit = 0
    portfolio = []

    for i in range(len(stocks)):
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
    return output


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

print(maximise_1c(json))