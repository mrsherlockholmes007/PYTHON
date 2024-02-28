def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False


def get_user_input():
    print("Enter the Sudoku board. Use 0 for empty cells.")
    board = []
    for i in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board


if __name__ == "__main__":
    user_board = get_user_input()
    print("\nInput Sudoku board:")
    print_board(user_board)

    solve(user_board)
    print("\nSolving...\n")
    print_board(user_board)

    print("\nSolved!")
