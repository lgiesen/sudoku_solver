# 18:28 Uhr

sudoku_board = [
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 8, 0, 4, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 9],

    [0, 0, 0, 9, 7, 4, 0, 0, 0],
    [3, 0, 1, 0, 8, 0, 0, 0, 0],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],

    [0, 0, 0, 4, 0, 0, 8, 0, 0],
    [0, 5, 6, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 1],
]


def solve(board):
    empty = find_empty(board)
    # base case: sudoku_board completely solved
    if not empty:
        return True
    # sudoku_board not solved
    else:
        x, y = empty
    # try possible solutions
    for num in range(1, 10):
        if valid(board, num, (x, y)):
            board[x][y] = num
            # recursion starts here: check next empty field
            if solve(board):
                return True
            # there is no possible solution for current field
            # -> backtracking: undo the last choice/action
            board[x][y] = 0
    return False


def valid(board, num, position):
    # check horizontal/row
    # using len(), if one wants to enlarge the sudoku
    # index != x -> do not check with the field you have just filled in
    for index in range(len(board[0])):
        if (num == board[position[0]][index]) and (index != position[1]):
            return False

    # check vertical/column
    # index != y -> do not check with the field you have just filled in
    for index in range(len(board)):
        if (num == board[index][position[1]]) and (index != position[0]):
            return False

    # check 3x3 box
    box_x = position[1] // 3
    box_y = position[0] // 3
    # box result: xy
    # 00 01 02
    # 10 11 12
    # 20 21 22
    # because we just integer-divided by 3, we have to multiply by 3
    # in order to get to the correct index
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False
    return True


# x is col, y = row
def print_board(board):
    for x in range(len(board)):
        # divide each 3x3 box
        # horizontal line (x != 0 -> do not print line above grid)
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - -")
        # vertical line (j != 0 -> do not print line left to the grid)
        for y in range(len(board[0])):
            if y % 3 == 0 and y != 0:
                # , end="" -> stay in the same line
                print(" | ", end="")
            # print numbers
            if y == 8:
                print(board[x][y])
            else:
                print(str(board[x][y]) + " ", end="")


def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                # returning in that order: row, col
                return y, x
    return None


print_board(sudoku_board)
print("_______________________")
solve(sudoku_board)
print_board(sudoku_board)