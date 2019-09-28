def chess(test):

    # [ROW, COL]

    queen = []
    n = len(test)
    for y in range(len(test)):
        for x in range(len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]
    
    # TOP
    top = 0
    for i in range(queen[0]-1,0,-1):
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
    for i in range(queen[1]-1,0,-1):
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
    temp_queen_row = queen[0]
    temp_queen_col = queen[1]
    for i in range(min(queen[0]-1,queen[1]-1),0,-1):
        temp_queen_row -= 1
        temp_queen_col -= 1
        if test[temp_queen_row][temp_queen_col] != "X":
            topleft += 1
        else:
            break
    
    # TOPRIGHT
    topright = 0
    temp_queen_row = queen[0]
    temp_queen_col = queen[1]
    for i in range(min(queen[0]-1,n-queen[1]),0,-1):
        temp_queen_row -= 1
        temp_queen_col -= 1
        if test[temp_queen_row][temp_queen_col] != "X":
            topright += 1
        else:
            break

    # DOWNLEFT
    downleft = 0
    temp_queen_row = queen[0]
    temp_queen_col = queen[1]
    for i in range(min(n-queen[0],queen[1]-1),0,-1):
        temp_queen_row -= 1
        temp_queen_col -= 1
        if test[temp_queen_row][temp_queen_col] != "X":
            downleft += 1
        else:
            break

    # DOWNRIGHT
    downright = 0
    temp_queen_row = queen[0]
    temp_queen_col = queen[1]
    for i in range(min(n-queen[0],n-queen[1]),0,-1):
        temp_queen_row -= 1
        temp_queen_col -= 1
        if test[temp_queen_row][temp_queen_col] != "X":
            downleft += 1
        else:
            break

    return top+topleft+topright+left+right+down+downleft+downright





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

print(chess(test))