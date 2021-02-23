def best_move(board, state_calculator):
    move = 0
    best_score = -999
    for i in range(len(board)):
        if board[i] == 0:
            temp_score = maximize(board, state_calculator)
            if temp_score > best_score:
                best_score = temp_score
                move = i
    return move


def maximize(board, state_calculator):
    tmp_state = state_calculator(board)
    if tmp_state == 'X':
        return 1
    if tmp_state == '0':
        return -1
    if tmp_state == 'draw':
        return 0

    score = -999
    for i in range(len(board)):
        if board[i] == 0:
            board[i] = 1
            temp_score = minimize(board, state_calculator)
            score = max(temp_score, score)
            board[i] = 0

    return score


def minimize(board, state_calculator):
    tmp_state = state_calculator(board)
    if tmp_state == 'X':
        return 1
    if tmp_state == '0':
        return -1
    if tmp_state == 'draw':
        return 0

    score = 999
    for i in range(len(board)):
        if board[i] == 0:
            board[i] = 2
            temp_score = maximize(board, state_calculator)
            score = min(temp_score, score)
            board[i] = 0

    return score

