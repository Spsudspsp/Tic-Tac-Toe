import random
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

while True:
    row = int(input('Select input position (row): '))
    col = int(input('Select input position (col): '))

    if board[row][col] == '-':
        board[row][col] = 'X'
        p_board = f'{board[0]}\n{board[1]}\n{board[2]}'


        r1x = True if board[0][0] == "X" and board[0][1] == 'X' and board[0][2] == 'X' else False
        r2x = True if board[1][0] == "X" and board[1][1] == 'X' and board[1][2] == 'X' else False
        r3x = True if board[2][0] == "X" and board[2][1] == 'X' and board[2][2] == 'X' else False
        c1x = True if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' else False
        c2x = True if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' else False
        c3x = True if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' else False
        d1x = True if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' else False
        d2x = True if board[0][2] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' else False
        r1o = True if board[0][0] == "O" and board[0][1] == 'O' and board[0][2] == 'O' else False
        r2o = True if board[1][0] == "O" and board[1][1] == 'O' and board[1][2] == 'O' else False
        r3o = True if board[2][0] == "O" and board[2][1] == 'O' and board[2][2] == 'O' else False
        c1o = True if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' else False
        c2o = True if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' else False
        c3o = True if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O' else False
        d1o = True if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' else False
        d2o = True if board[0][2] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' else False


        print(p_board)
        if r1x or r2x or r3x or c1x or c2x or c3x or d1x or d2x:
            exit('Player victory.')
        elif r1o or r2o or r2o or c1o or c2o or c3o or d1o or d2o:
            exit('AI victory.')

    else:
        print('INDEX ALREADY OCCUPIED')
        continue

    while True:
        bot_row, bot_col = random.randint(0, 2), random.randint(0, 2)
        if board[bot_row][bot_col] == '-':
            board[bot_row][bot_col] = 'O'
            p_2board = f'{board[0]}\n{board[1]}\n{board[2]}'
            print(p_2board)
            break
        else: continue