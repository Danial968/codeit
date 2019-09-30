import itertools

def guncontrol(test):
    #test = request.json
    #print(test)
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

    def moveEnd(currentPoint,grid,gridVisit,endpointNfuel,fuel,maxfuel):
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
            moveEnd((y-1,x),grid,gridVisit,endpointNfuel,fuel,maxfuel)
        if moveright:
            moveEnd((y,x+1),grid,gridVisit,endpointNfuel,fuel,maxfuel)
        if movebot:
            moveEnd((y+1,x),grid,gridVisit,endpointNfuel,fuel,maxfuel)
        if moveleft:
            moveEnd((y,x-1),grid,gridVisit,endpointNfuel,fuel,maxfuel)

        if (not movetop) and (not moveright) and (not movebot) and (not moveleft):
            # add to endpoint
            if fuel <= maxfuel:
                endpointNfuel += [((y,x),fuel)]

    moveEnd((0,0),grid,gridVisit,endpointNfuel,0,fuel)
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
    # for i in range(len(endpointNfuel)):
    #     perms = itertools.permutations(endpointNfuel,i)
    #     for setlist in list(perms):
    #         if sum(map(lambda x: x[1], setlist)) == fuel:
    #             final = setlist
    
    
    for i in range(len(endpointNfuel)):
        nextbest = 0
        nextFinal = [endpointNfuel[i]]
        for j in range(len(endpointNfuel)):
            if i != j:
                add = nextFinal + [endpointNfuel[j]]
                fueltotal = 0
                for it in add:
                    fueltotal += it[1]
                if fueltotal == fuel:
                    hits = []
                    for item in nextFinal:
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
                    print(fuel,sum(map(lambda x:x[1], nextFinal)))
                    return output
                if fueltotal <= fuel and fueltotal > nextbest:
                    nextFinal += [endpointNfuel[j]]
                    nextbest = fueltotal
                elif fueltotal > fuel:
                    break
        if sum(map(lambda x:x[1], final)) < nextbest:
            final =  nextFinal




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
    print(fuel,sum(map(lambda x:x[1], final)))
    return output
    #return jsonify(output)

test = { 
  "grid":[ 
    "OOXXOO",
    "XOOOOX",
    "XOXXOX",
    "OOXOOO",
    "OXOOXO"
  ],
  "fuel":15
}
test2 = {'grid': ['OXXXXXXXXXOXOXOXOX', 'OXXXXXXXXXOXOXOXOX', 'OXXXXXXXXXOXOXOXOX', 'OXXXXXXXXXOXOXOXOX', 'OXXXXXXXXXOXOXOXOX', 'OXXXXXXXXXOXOXOXOX', 'OXXXXXOOOOOXOXOXOX', 'OXXXXXOXOXOXOXOXOX', 'OOOOOOOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOX', 'XXXXXXXXXXOXOXOXOX', 'XXXXXXXXXXOXOXOXOX', 'XXXXXXXXXXOOOOOXOX', 'XXXXXXXXXXOXOXOXOX', 'XXXXXXXXXXOXOXOXOX', 'XXXXXXXXXXOXOXOXOX', 'XXXXXXXXXXOXOXOOOX', 'XXXXXXXXXXXXXXXXXX'], 'fuel': 63}
#print(guncontrol(test))

test3 = {'grid': ['OOOOOXXXXXXXOOOOOOOXOXOOOX', 'XXXXOXXXXXXXOXOXOXOXOXOXOX', 'XXXXOXXXXXXXOXOXOXOXOXOXOX', 'XXXXOXXXXXXXOXOXOXOXOXOXOX', 'XXXXOXXXXXXXOXOXOXOOOOOXOX', 'XXXXOXXXXXXXOXOXOXOXOXOXOX', 'XXXXOOOOOOOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOOOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXOXOXOXOXOXOXOXOX', 'XXXXXXXXXXXXXXXXXXXXXXXXXX'], 'fuel': 251}   
#print(guncontrol(test3))

test4 ={'grid': ['OOOOOXOOOOOOOXOXOOOXOXOOOXO', 'XXXXOXOXXXOXOXOXOXOXOXOXOXO', 'XXXXOOOXXXOXOXOXOXOOOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOOOXOOO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOOOOOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXOXOXOXOXOXOXOXO', 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'], 'fuel': 394}
print(guncontrol(test4))
