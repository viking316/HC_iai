def nextMove(player, board):
    def is_winner(b, p):
        # Check rows, columns, and diagonals for a winning move
        for i in range(3):
            if all(b[i][j] == p for j in range(3)):  # Check row
                return True
            if all(b[j][i] == p for j in range(3)):  # Check column
                return True
        if all(b[i][i] == p for i in range(3)):      # Check main diagonal
            return True
        if all(b[i][2 - i] == p for i in range(3)):  # Check anti-diagonal
            return True
        return False

    def find_winning_move(b, p):
        for r in range(3):
            for c in range(3):
                if b[r][c] == '_':
                    b[r][c] = p
                    if is_winner(b, p):
                        b[r][c] = '_'  # Reset the move
                        return r, c
                    b[r][c] = '_'  # Reset the move
        return None

    # Check for a winning move for the player
    winning_move = find_winning_move(board, player)
    if winning_move:
        print(f"{winning_move[0]} {winning_move[1]}")
        return

    # Check for a winning move for the opponent and block it
    opponent = 'O' if player == 'X' else 'X'
    blocking_move = find_winning_move(board, opponent)
    if blocking_move:
        print(f"{blocking_move[0]} {blocking_move[1]}")
        return

    # Make the first available move
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                print(f"{r} {c}")
                return

# Input handling
player = input().strip()
board = []
for _ in range(3):
    board.append(list(input().strip()))

nextMove(player, board)
