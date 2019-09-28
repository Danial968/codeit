def primo(test):

    initial = test["initial"]
    goal = test["goal"]
    current = initial
    moves = []

    while(current != goal):
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