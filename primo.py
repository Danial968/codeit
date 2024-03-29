def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0

def primo(test):

    initial = test["initial"]
    goal = test["goal"]
    print(initial)
    print(goal)
    current = initial
    moves = []

    depthini = depth(initial)

    while(current != goal):
        if depthini == 1:
            if 0 in current:
                current_index = [current.index(0)]
            num_at_goal = goal[current_index[0]]
            if num_at_goal in current:
                to_move = [current.index(num_at_goal)]
            if to_move[0] < current_index[0]:
                moves.append("L")
                current[to_move[0]], current[current_index[0]] = current[current_index[0]], current[to_move[0]]
            else:
                moves.append("R")
                current[to_move[0]], current[current_index[0]] = current[current_index[0]], current[to_move[0]]
        elif depthini == 2:
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
        else:
            for n in range(len(current)):
                for i in range(len(current[n])):
                    if 0 in current[n][i]:
                        current_index = [n, i, current[n][i].index(0)]
                        break
            num_at_goal = goal[current_index[0]][current_index[1]][current_index[2]]
            for n in range(len(current)):
                for i in range(len(current[n])):
                    if num_at_goal in current[n][i]:
                        to_move = [n, i, current[n][i].index(num_at_goal)]
                        break
            if to_move[0] == current_index[0]:
                if to_move[1] == current_index[1]:
                    if to_move[2] < current_index[2]:
                        moves.append("L")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                    else:
                        moves.append("R")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                else:
                    if to_move[1] < current_index[1]:
                        moves.append("B")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                    else:
                        moves.append("F")
                        current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
            else:
                if to_move[0] < current_index[0]:
                    moves.append("D")
                    current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
                else:
                    moves.append("U")
                    current[to_move[0]][to_move[1]][to_move[2]], current[current_index[0]][current_index[1]][current_index[2]] = current[current_index[0]][current_index[1]][current_index[2]], current[to_move[0]][to_move[1]][to_move[2]]
    return moves
test = {
  "initial": [[2, 5, 7, 3], [9, 1, 14, 4], [10, 11, 15, 8], [6, 13, 0, 12]],
  "goal": [[2, 6, 5, 7], [1, 8, 3, 4], [13, 9, 14, 11], [0, 15, 12, 10]]
}

print(primo(test))