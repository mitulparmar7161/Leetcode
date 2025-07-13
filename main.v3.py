from Chessnut import Game
import random

# Piece values for material evaluation
PIECE_VALUES = {"p": 1, "n": 3, "b": 3.3, "r": 5, "q": 9, "k": 0}

# Function to check if a pawn can be promoted
def can_promote(fen, color):
    """
    Check if a pawn is eligible for promotion.
    """
    board = fen.split()[0].split("/")  # Split FEN string into rows
    promotion_rank = 6 if color == "white" else 1  # 7th rank for white, 2nd rank for black

    # Get the promotion rank (7th for white, 2nd for black)
    rank = board[promotion_rank]

    # Loop through the squares on the promotion rank
    for i in range(len(rank)):  # Iterate through each square in the rank
        # Check for white or black pawn on the correct promotion rank
        if (color == "white" and rank[i] == "p") or (color == "black" and rank[i] == "P"):
            return True  # A pawn is ready for promotion
    return False

# Function to identify high-value targets (Queen or Rook)
def find_opponent_high_value_pieces(fen, color):
    """
    Identify and return positions of the opponent's queen and rooks.
    """
    opponent_color = "black" if color == "white" else "white"
    opponent_pieces = {"q", "r"} if opponent_color == "white" else {"Q", "R"}
    
    board = fen.split()[0].split("/")  # Split FEN string into rows
    high_value_positions = []

    for row_index, row in enumerate(board):
        for col_index, piece in enumerate(row):
            if piece.lower() in opponent_pieces:
                high_value_positions.append((row_index, col_index, piece))  # Store position and piece type

    return high_value_positions

# Function to prioritize eliminating opponent's queen and rook
def prioritize_eliminating_high_value(fen, color):
    """
    Prioritize moves that eliminate the opponent's queen and rook.
    """
    high_value_pieces = find_opponent_high_value_pieces(fen, color)
    if not high_value_pieces:
        return None  # No high-value pieces to target

    # Check for moves that threaten the opponent's high-value pieces
    game = Game(fen)
    moves = list(game.get_moves())
    random.shuffle(moves)

    for move in moves:
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)
        
        # Check if this move results in the capture of an opponent's high-value piece
        for piece in high_value_pieces:
            row, col, target_piece = piece
            if target_piece == "q" and game_copy.get_fen().split()[0][row * 8 + col] == "Q":  # Capturing the opponent's queen
                return move
            elif target_piece == "r" and game_copy.get_fen().split()[0][row * 8 + col] == "R":  # Capturing the opponent's rook
                return move

    return None  # No direct elimination found, proceed with other strategies

# Function to prioritize pawn advancement (with a fallback)
def prioritize_pawn_advancement(game, color):
    """
    Find the best move for advancing pawns, focusing on promoting pawns to queens.
    """
    moves = list(game.get_moves())
    random.shuffle(moves)  # Add randomness to handle ties more naturally
    best_move = None

    for move in moves:
        game_copy = Game(game.get_fen())
        game_copy.apply_move(move)

        if can_promote(game_copy.get_fen(), color):  # If pawn promotion is possible
            return move  # Prioritize promoting pawns to queens

    return None  # Return None if no promotion is possible but keep searching for other moves

# Main function to control the chess bot
def chess_bot(obs):
    """
    Chess bot that always promotes pawns to queens and eliminates the opponent's high-value pieces (queen and rook).
    """
    game = Game(obs.board)
    moves = list(game.get_moves())

    if not moves:
        return None  # No valid moves, should never happen unless game over

    # Determine bot's color
    color = "white" if game.get_fen().split()[1] == "w" else "black"

    # First, prioritize capturing the opponent's queen and rook
    move = prioritize_eliminating_high_value(game.get_fen(), color)
    if move:
        return move  # If a move eliminates a high-value piece, prioritize it

    # Otherwise, apply pawn advancement strategy
    move = prioritize_pawn_advancement(game, color)
    if move:
        return move  # If a move promotes a pawn, prioritize it

    # If no pawn advancement or high-value piece elimination is found, fall back to random valid move
    return random.choice(moves)
