def primo(test):

    initial = test["initial"]
    goal = test["goal"]
    print(initial)
    current = initial
    moves = []

    while(current != goal):
        for n in range(len(current)):
            for i in range(len(current[n])):
                if 0 in current[n][i]:
                    current_index = [n, i, current[i].index(0)]
                    break
        num_at_goal = goal[current_index[0]][current_index[1]][current_index[2]]
        for n in range(len(current)):
            for i in range(len(current[n])):
                if num_at_goal in current[n][i]:
                    to_move = [n, i, current[i].index(num_at_goal)]
                    break
        if to_move[0] == current_index[0]:
            if to_move[1] == current_index[1]:
                if to_move[2] < current_index[2]:
                    moves.append("L")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
                else:
                    moves.append("R")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
            else:
                if to_move[1] < current_index[1]:
                    moves.append("B")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
                else:
                    moves.append("F")
                    current[to_move[0]][to_move[1]], current[current_index[0]][current_index[1]] = current[current_index[0]][current_index[1]], current[to_move[0]][to_move[1]]
        else:
            if to_move[0] < current_index[0]:
                moves.append("L")
    return moves
test = {
  "initial": [[ 1, 2, 3, 4],
              [ 5, 6, 7, 8],
              [ 9,10,12, 0],
              [13,14,11,15]],
  "goal": [[ 1, 2, 3, 4],
           [ 5, 6, 7, 8],
           [ 9,10,11,12],
           [13,14,15, 0]]
}

print(primo(test))