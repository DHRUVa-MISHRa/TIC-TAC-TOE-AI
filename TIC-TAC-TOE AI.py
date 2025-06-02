def print_board(board):
    print()
    for i in range(3):
        row = ' | '.join(board[i*3:(i+1)*3])
        print(' ' + row)
        if i < 2:
            print('-----------')
    print()

def is_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def is_draw(board):
    return all(s != ' ' for s in board)

def minimax(board, depth, is_maximizing, ai_player, human_player):
    if is_winner(board, ai_player):
        return 10 - depth
    if is_winner(board, human_player):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = ai_player
                score = minimax(board, depth+1, False, ai_player, human_player)
                board[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = human_player
                score = minimax(board, depth+1, True, ai_player, human_player)
                board[i] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def get_ai_move(board, ai_player, human_player):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai_player
            score = minimax(board, 0, False, ai_player, human_player)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[move-1] != ' ':
                print("Spot already taken. Choose another.")
                continue
            return move-1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    board = [' ']*9
    human_player = ''
    ai_player = ''
    while human_player not in ['X','O']:
        human_player = input("Choose your mark (X/O): ").upper()
    ai_player = 'O' if human_player == 'X' else 'X'

    # Decide who goes first: Human for X else AI for X
    turn = 'X'

    print_board(board)

    while True:
        if turn == human_player:
            print("Your turn.")
            move = get_human_move(board)
            board[move] = human_player
        else:
            print("AI's turn.")
            move = get_ai_move(board, ai_player, human_player)
            board[move] = ai_player

        print_board(board)

        if is_winner(board, turn):
            if turn == human_player:
                print("Congratulations! You win!")
            else:
                print("AI wins! Better luck next time.")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        turn = human_player if turn == ai_player else ai_player

    print("Game over.")

if __name__ == '__main__':
    play_game()

