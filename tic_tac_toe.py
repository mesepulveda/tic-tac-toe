"""Very simple tic tac toe game."""


def print_board(board):
    """Prints in the terminal the board."""
    print('  | 1 | 2 | 3')
    for row in range(3):
        print('-'*14)
        print(str(row + 1), '|', ' | '.join(board[row]))


def input2list(input_text):
    """Converts the input from text to a list of coordinates."""
    input_list = input_text.strip().split(',')
    input_list = [int(i) - 1 for i in input_list]
    for val in input_list:
        if val not in range(3):
            raise ValueError
    return input_list


def add_mark(board, mark, player):
    """Adds a the player in the mark coordinate of the board."""
    board[mark[0]][mark[1]] = player
    return board


def valid_mark(board, mark):
    """Checks if the new mark point is valid."""
    if board[mark[0]][mark[1]] == ' ':
        return True
    return False


def check_win(board):
    """Checks if the player already won."""
    # Check row
    for i in range(3):
        if check_line(board[i]):
            return True
    # Check column
    transposed_board = transpose(board)
    for i in range(3):
        if check_line(transposed_board[i]):
            return True
    # Check diagonals
    if check_line([board[0][0], board[1][1], board[2][2]]):
        return True
    if check_line([board[0][2], board[1][1], board[2][0]]):
        return True
    return False


def check_line(line):
    """Checks one line of the board looking for a winner."""
    if line[0] == line[1] and line[1] == line[2]:
        if line[0] != ' ':
            return True
    return False


def transpose(board):
    """Returns a transposed board."""
    transposed_board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(board[j][i])
        transposed_board.append(row)
    return transposed_board


def get_user_input(board):
    """Gets the user input and handles the errors."""
    while True:
        try:
            mark = input2list(input('Choose where to mark (R, C): '))
            # check if it is valid
            if valid_mark(board, mark):
                break
            print('Invalid mark, try again')
        except (ValueError, IndexError):
            print('Invalid mark, try again')
    return mark


def clear_console():
    """prints vertical space to 'clear console'."""
    print('\n'*60)


def print_congratulations():
    print()
    print('*'*29)
    print('* Congratulations, you win! *')
    print('*'*29)
    print()


def main():
    clear_console()
    board = [[' ']*3 for i in range(3)]
    game_over = False
    while not game_over:
        for player in ['X', 'O']:
            # show the board
            print_board(board)
            # ask for input
            mark = get_user_input(board)
            clear_console()
            # add the mark to the board
            board = add_mark(board, mark, player)
            # check if the player won
            game_over = check_win(board)
            if game_over:
                print_board(board)
                print_congratulations()
                break


if __name__ == '__main__':
    main()
