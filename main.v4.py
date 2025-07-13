from Chessnut import Game
import random

# Material evaluation function
def material_evaluation(board):
    piece_values = {'p': 1, 'r': 5, 'n': 3, 'b': 3, 'q': 9, 'k': 100}  # Simplified piece values
    evaluation = 0

    for piece in board.pieces:
        if piece.color == "w":  # White pieces
            evaluation += piece_values.get(piece.piece_type, 0)
        else:  # Black pieces
            evaluation -= piece_values.get(piece.piece_type, 0)

    return evaluation

# Minimax search to evaluate a move (simplified for time/space efficiency)
# Minimax search to evaluate a move (simplified for time/space efficiency)
def minimax(game, depth, maximizing_player, alpha=-float('inf'), beta=float('inf')):
    # Check if we should stop the search (either depth is 0 or game is over)
    if depth == 0 or game.status in [Game.CHECKMATE, Game.STALEMATE]:
        return material_evaluation(game.board)

    legal_moves = game.get_moves()
    if maximizing_player:
        max_eval = -float('inf')
        for move in legal_moves:
            game_copy = Game(game.board.fen())
            game_copy.apply_move(move)
            eval = minimax(game_copy, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            game_copy = Game(game.board.fen())
            game_copy.apply_move(move)
            eval = minimax(game_copy, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval



def chess_bot(obs):
    """
    A chess bot that uses material evaluation and basic minimax to decide its moves.

    Args:
        obs: An object with a 'board' attribute representing the current board state as a FEN string.

    Returns:
        A string representing the chosen move in UCI notation (e.g., "e2e4")
    """
    # Parse the current board state and generate legal moves using Chessnut library
    game = Game(obs.board)
    legal_moves = list(game.get_moves())

    # Basic strategy for checkmate
    for move in legal_moves[:10]:
        g = Game(obs.board)
        g.apply_move(move)
        if g.status == Game.CHECKMATE:
            return move

    # Use minimax with depth 2 to select the best move
    best_move = None
    best_value = -float('inf')

    for move in legal_moves:
        game_copy = Game(obs.board)
        game_copy.apply_move(move)
        move_value = minimax(game_copy, 2, False)  # Depth 2 for simplicity
        if move_value > best_value:
            best_value = move_value
            best_move = move

    # Return the best move found through evaluation
    return best_move if best_move else random.choice(legal_moves)




