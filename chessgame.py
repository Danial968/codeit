def chessgame(test):

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
    return top+top_left+top_right+right+left+down+down_left+down_right

test =[
      [
        "","K","","",""
      ],
      [
        "","","","",""
      ],
      [
        "X","X","","",""
      ],
      [
        "","","X","",""
      ],
      [
        "","","","",""
      ] 
    ]

print(chessgame(test))



queen = []
    obstacles = []

    for y in range(len(test)):
        n = len(test)

        for x in range(len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]
            if test[y][x] == 'X':
                obstacles.append([y+1,x+1])
    
    # print(queen)
    # print(obstacles)
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
    # print(obstacles)
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
            # print(obs)
            # print(queen)
            if(obs[1] > queen[1]):
                steps_right = obs[1] - queen[1] -1
                # right = False
            else:
                steps_left = queen[1] - obs[1] -1
                # print(obs)
                # print(queen)
                # left = False

        if obs[1] == queen[1]:
            if obs[0] > queen[0]:
                steps_down = obs[0] - queen[0] - 1
            else:
                steps_up = queen[0] - obs[0] - 1
                # print(queen[0])
                # print(obs[0])
                # up = False

        if(queen_diagonal_right != obs and queen_diagonal_right[1] <= n and diag_right_down):
            # print(queen_diagonal_right)
            diagonal_right += 1
        else:
            diag_right_down = False
        
        if(queen_diagonal_left != obs and queen_diagonal_left[1] > 0 and diag_left_down):
            # print(queen_diagonal_left)
            diagonal_left += 1
        else:
            diag_left_down = False

        if(queen_diagonal_right_up != obs and queen_diagonal_right_up[0] > 0 and diag_right_up):
            # print(queen_diagonal_right_up)
            diagonal_right_up += 1

        else:
            diag_left_up = False
        
        if(queen_diagonal_left_up != obs and queen_diagonal_left_up[0] > 0 and queen_diagonal_left_up[1] > 0 and diag_left_up):
            # print(queen_diagonal_left_up)
            diagonal_left_up += 1

        else:
            diag_left_up = False


    # print(steps_right)
    total = diagonal_left + diagonal_left_up + diagonal_right + diagonal_right_up + steps_down + steps_left + steps_right + steps_up