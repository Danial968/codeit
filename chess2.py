def chess(test):
    queen = []
    obstacles = []
    n = len(test[0])
    
    for y in range (len(test)):

        for x in range (len(test[y])):
            if test[y][x] == 'K':
                queen = [y+1, x+1]
            if test[y][x] == 'X':
                obstacles.append([y+1, x+1])

    step_up = queen[0] - 1
    step_down = n - queen[0]

    step_right = n - queen[1]
    step_left = queen[1] - 1

    for obs in obstacles:

        if obs[0] == queen[0]:

            if obs[1] < queen[1] and ((queen[1] -obs[1] -1 ) < step_left):
                step_left = queen[1] - obs[1] -1

            if obs[1] > queen[1] and ((obs[1]- queen[1] - 1) < step_right ):
                step_right = obs[1] - queen[1] - 1

        if obs[1] == queen[1]:

            if obs[0] < queen[0] and ((queen[0] - obs[0] - 1) <step_up):
                step_up = queen[0] - obs[0] - 1

            if obs[0] > queen[0] and (( obs[0] -queen[0] -  1) > step_down):
                step_down =  obs[0] -queen[0] -  1
    print(step_down)

chess(    [
      [
        "","","","",""
      ],
      [
        "","","","",""
      ],
      [
        "X","","K","",""
      ],
      [
        "","","X","",""
      ],
      [
        "","","","",""
      ] 
    ])