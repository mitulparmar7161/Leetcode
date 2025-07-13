from Chessnut import Game
import random

# Piece values for material evaluation
PIECE_VALUES = {"p": 1, "n": 3, "b": 3.3, "r": 5, "q": 9, "k": 0}

def evaluate_board(fen, color):
    """
    Evaluate the board state based on material balance.
    """
    board = fen.split()[0].replace("/", "")  # Simplify FEN board
    score = 0
    for char in board:
        if char.isalpha():
            value = PIECE_VALUES[char.lower()]
            if char.isupper() == (color == "white"):  # Check piece ownership
                score += value
            else:   
                score -= value
    return score

def get_best_move(game, depth, color):
    """
    Evaluate a limited number of moves and choose the best one.
    """
    moves = list(game.get_moves())
    random.shuffle(moves)  # Add randomness to handle ties more naturally
    best_move = None
    best_value = float("-inf") if color == "white" else float("inf")

    for move in moves[:15]:  # Limit to top 15 moves for efficiency
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        value = evaluate_board(game_copy.get_fen(), color)
        if (color == "white" and value > best_value) or (color == "black" and value < best_value):
            best_value = value
            best_move = move
    return best_move

def chess_bot(obs):
    """
    Efficient chess bot implementation focusing on material balance and move pruning.
    """
    game = Game(obs.board)
    moves = list(game.get_moves())

    if not moves:
        return None  # No valid moves, should never happen unless game over

    # Determine bot's color
    color = "white" if game.get_fen().split()[1] == "w" else "black"

    # Evaluate moves for quick wins
    for move in moves:
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        if game_copy.status == Game.CHECKMATE:
            return move  # Instant win

    # Use lightweight evaluation for best move
    return get_best_move(game, depth=2, color=color)
