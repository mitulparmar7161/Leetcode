from Chessnut import Game
import random

# Piece values for material evaluation
PIECE_VALUES = {"p": 1, "n": 3, "b": 3.3, "r": 5, "q": 9, "k": 0}

# Function to evaluate the board based on material count
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

# Function to determine a good move based on board evaluation
def get_best_move(game, color):
    """
    Evaluate a set of possible moves and choose the best one.
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

# Opening strategy
OPENINGS = {
    "1. e4 e5 2. Nf3 Nc6 3. Bb5": "Ruy Lopez",
    "1. e4 e5 2. Nf3 Nc6 3. Bc4": "Italian Game",
    "1. d4 d5 2. c4": "Queen's Gambit",
}

# Function to return the opening move based on common openings
def apply_opening(game):
    """
    Apply an opening move if possible.
    """
    fen_history = game.fen_history  # No parentheses, because fen_history is a list
    opening_moves = {
        "e2e4": "e7e5",  # White opens with e4, Black responds with e5
        "e7e5": "g1f3",  # White responds with Nf3
        "g1f3": "b8c6",  # Black responds with Nc6
        "b8c6": "f1b5",  # White plays Bb5
    }

    if len(fen_history) == 0:
        return "e2e4"  # White's opening move
    elif len(fen_history) == 1 and fen_history[0] == "e2e4":
        return "e7e5"  # Black's response to 1. e4
    elif len(fen_history) == 2 and fen_history[1] == "e7e5":
        return "g1f3"  # White's second move
    elif len(fen_history) == 3 and fen_history[2] == "g1f3":
        return "b8c6"  # Black's second move
    elif len(fen_history) == 4 and fen_history[3] == "b8c6":
        return "f1b5"  # White plays Bb5 (Ruy Lopez)

    # If no opening is possible, fallback to random move
    return random.choice(game.get_moves())

# Main function to control the chess bot
def chess_bot(obs):
    """
    Efficient chess bot with advanced opening and material evaluation.
    """
    game = Game(obs.board)
    moves = list(game.get_moves())

    if not moves:
        return None  # No valid moves, should never happen unless game over

    # Determine bot's color
    color = "white" if game.get_fen().split()[1] == "w" else "black"

    # First apply opening moves if possible
    move = apply_opening(game)
    if move:
        return move

    # Evaluate moves for quick wins
    for move in moves:
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        if game_copy.status == Game.CHECKMATE:
            return move  # Instant win

    # Use lightweight evaluation for best move
    return get_best_move(game, color)
