def best_move(board, state_calculator):
    # todo scoate asta si baga alegerea aia ca lumea
    maximize(board, state_calculator)
    for i in range(len(board)):
        if board[i] == 0:
            return i


def maximize(board, state_calculator):
    pass


def minimize(board):
    pass

