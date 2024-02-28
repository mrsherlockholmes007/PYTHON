import chess
import random

def evaluate_board(board):
    evaluation = 0
    piece_map = board.piece_map()
    for square, piece in piece_map.items():
        if piece.color == chess.WHITE:
            evaluation += piece.piece_type
        else:
            evaluation -= piece.piece_type
    return evaluation

def generate_moves(board):
    return [move for move in board.legal_moves]

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in generate_moves(board):
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
        for move in generate_moves(board):
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def play_computer_move(board, difficulty):
    if difficulty == 1:
        return random.choice(list(board.legal_moves))
    elif difficulty == 2:
        best_move = None
        max_eval = float('-inf')
        for move in generate_moves(board):
            board.push(move)
            eval = minimax(board, 2, float('-inf'), float('inf'), False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move
    elif difficulty == 3:
        best_move = None
        max_eval = float('-inf')
        for move in generate_moves(board):
            board.push(move)
            eval = minimax(board, 3, float('-inf'), float('inf'), False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move

def print_board(board):
    print('   a b c d e f g h')
    print('  +----------------')
    for i in range(8, 0, -1):
        row = f'{i} |'
        for j in range(1, 9):
            piece = board.piece_at(chess.square(j - 1, i - 1))
            if piece is None:
                row += ' '
            else:
                row += piece.symbol()
            row += '|'
        print(row)
        print('  +----------------')

def play_game():
    board = chess.Board()
    difficulty = int(input("Choose difficulty level (1-3): "))
    
    while not board.is_game_over():
        print_board(board)
        valid_move = False
        while not valid_move:
            player_move = input("Enter your move: ")
            if chess.Move.from_uci(player_move) in board.legal_moves:
                valid_move = True
            else:
                print("Invalid move. Please try again.")
        board.push_san(player_move)
        print_board(board)
        computer_move = play_computer_move(board, difficulty)
        print(f"Computer's next move: {chess.Move.uci(computer_move)}")  # Display computer's next move
        board.push(computer_move)

    print("Game Over. Result:", board.result())
play_game()
