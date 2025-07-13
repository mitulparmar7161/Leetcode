import chess
import random

# Piece values for material evaluation
PIECE_VALUES = {
    "p": 1, "n": 3, "b": 3.3, "r": 5, "q": 9, "k": 0
}

# Piece-square tables for positional evaluation
PIECE_SQUARE_TABLES = {
    "P": [
         0,  5,  5,  0,  5, 10, 50,  0,
         0, 10, -5,  0,  5, 10, 50,  0,
         0,  5, -10, 0,  5, 10, 50,  0,
         0,  0,  0, 20, 30, 30, 50,  0,
         0,  5,  5, 10, 25, 30, 50,  0,
         0,  5,  5,  0, 20, 20, 50,  0,
         0,  0,  0,  0, 10, 10, 50,  0,
         0,  0,  0,  0,  0,  0, 50,  0
    ],
    "N": [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20,   0,   5,   5,   0, -20, -40,
        -30,   5,  10,  15,  15,  10,   5, -30,
        -30,   0,  15,  20,  20,  15,   0, -30,
        -30,   5,  15,  20,  20,  15,   5, -30,
        -30,   0,  10,  15,  15,  10,   0, -30,
        -40, -20,   0,   0,   0,   0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50
    ],
    "B": [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10,   5,   0,   0,   0,   0,   5, -10,
        -10,  10,  10,  10,  10,  10,  10, -10,
        -10,   0,  10,  10,  10,  10,   0, -10,
        -10,   5,   5,  10,  10,   5,   5, -10,
        -10,   0,   5,  10,  10,   5,   0, -10,
        -10,   0,   0,   0,   0,   0,   0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20
    ],
    "R": [
          0,   0,   0,   5,   5,   0,   0,   0,
         -5,   0,   0,   0,   0,   0,   0,  -5,
         -5,   0,   0,   0,   0,   0,   0,  -5,
         -5,   0,   0,   0,   0,   0,   0,  -5,
         -5,   0,   0,   0,   0,   0,   0,  -5,
         -5,   0,   0,   0,   0,   0,   0,  -5,
          5,  10,  10,  10,  10,  10,  10,   5,
          0,   0,   0,   5,   5,   0,   0,   0
    ],
    "Q": [
        -20, -10, -10,  -5,  -5, -10, -10, -20,
        -10,   0,   5,   0,   0,   0,  -5, -10,
        -10,   5,   5,   5,   5,   5,   0, -10,
         -5,   0,   5,   5,   5,   5,   0,  -5,
          0,   0,   5,   5,   5,   5,   0,  -5,
        -10,   0,   5,   5,   5,   5,   0, -10,
        -10,   0,   0,   0,   0,   0,   0, -10,
        -20, -10, -10,  -5,  -5, -10, -10, -20
    ],
    "K": [
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -10, -20, -20, -20, -20, -20, -20, -10,
         20,  20,   0,   0,   0,   0,  20,  20,
         20,  30,  10,   0,   0,  10,  30,  20
    ],
}

# Heuristic evaluation function
def evaluate_board(board):
    score = 0
    for square, piece in board.piece_map().items():
        value = PIECE_VALUES[piece.symbol().lower()]
        position_score = PIECE_SQUARE_TABLES.get(piece.symbol(), [0] * 64)[square]
        if piece.color == chess.WHITE:
            score += value + position_score
        else:
            score -= value + position_score
    return score

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)
    if maximizing:
        max_eval = -float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Select the best move
def select_best_move(board, max_depth=3):
    best_move = None
    best_value = -float('inf') if board.turn else float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, max_depth - 1, alpha, beta, not board.turn)
        board.pop()
        if (board.turn and eval > best_value) or (not board.turn and eval < best_value):
            best_value = eval
            best_move = move

    return best_move

# Main bot function
def chess_bot(obs):
    board = chess.Board(obs.board)
    return select_best_move(board, max_depth=3)
