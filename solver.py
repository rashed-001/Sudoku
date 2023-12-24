def solve(num):
    find = find_empty(num)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(num, i, (row, col)):
            num[row][col] = i

            if solve(num):
                return True

            num[row][col] = 0

    return False


def valid(mat, num, pos):
    # Check row
    for i in range(len(mat[0])):
        if mat[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(mat)):
        if mat[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if mat[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(mat):
    for i in range(len(mat)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(mat[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")


def find_empty(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return (i, j)  # row, col

    return None
