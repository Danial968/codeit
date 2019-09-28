def chess(test):
    queen = []
    obstacles = []

    for y in range(len(test)):
        n = len(test)

        for x in range(len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]
            if test[y][x] == 'X':
                obstacles.append([y+1,x+1])

    print(queen)
    print(obstacles)

test = [ 
    [
        "","","","",""
      ],
      [
        "","X","X","X","X"
      ],
      [
        "X","X","K","X",""
      ],
      [
        "","X","X","X","X"
      ],
      [
        "","","","",""
      ] 
    ]

# print(len(test))
chess(test)