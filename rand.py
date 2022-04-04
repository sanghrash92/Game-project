# def draw_board():
#     v = [' ' for _ in range(9)]
#     for row in [v[i*3:(i+1)*3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')
            
#     number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
#     for row in number_board:
#         print('| ' + ' | '.join(row) + ' |')
            
            
# draw_board()

# board = [
#     ["_", "_", "_"],
#     ["_", "_", "_"],
#     ["_", "_", "_"]
# ]

# def print_board():
#     for row in board:
#         print(row)
        
# print_board()


def main():
    # drawing a board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    is_x = True
    game_over = False
    while not game_over:
        print_board(board)
        try:
            selection = convert_selection(select_square())
            place_piece(selection, is_x, board)
        except ValueError:
            print('Sorry, please select a square 1-9 that is unoccupied.')
            continue
        game_over = is_draw(board)
        is_x = not is_x
        
def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
            print('Draw, no more moves.')
            return True
def is_win(board):
    winner = None
    for i in range(3):
        # horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        # vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    # diagonal
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2]
            or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(f"{winner} is the winner!")
        return True
    return False
    
# defining the outline of the board so we can call it 
def print_board(board):
    for row in board:
        print(row)

def convert_selection(selection):
    selection -= 1
    return (selection // 3, selection % 3)

def place_piece(selection, is_x, board):
    i, j = selection
    if board [i][j] == "_":
        board[i][j] = "X" if is_x else 'O'
    else:
        raise ValueError

# defining the selection of board to use it again
def select_square():
    selection = int(input('Select a square: '))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection

if __name__ == '__main__':
    main()




