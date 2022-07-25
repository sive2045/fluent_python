# buliding lists of list
board = [['_'] * 3 for _ in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# A list with three references to the same list is useless!!
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)