def best_move(board):
    for i in range(len(board)):
        if board[i] == 0:
            return i
