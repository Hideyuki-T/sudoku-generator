#!/usr/bin/env python3
import random
import copy

def create_board():
    """
    9×9の盤面を生成。初期状態は全て0。
    """
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board

def print_board(board):
    """
    盤面を表示する。0は空欄として'.'で表示する。
    """
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(board):
    """
    盤面内の空白セルを探す。
    空白が存在しない場合はNoneを返す。
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, row, col, num):
    """
    指定した数字numを (row, col) に配置した場合、ルールに反していないかをチェックする。
    """
    # 行
    if num in board[row]:
        return False

    # 列
    if num in [board[i][col] for i in range(9)]:
        return False

    # 3×3
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve(board):
    """
    バックトラッキング法を用いて盤面を数独に解決する。
    空のセルがなくなった時点でTrueを返し、解けない場合はFalseを返す。
    """
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # バックトラック
    return False

def generate_complete_board():
    """
    完全な盤面を生成して返す。
    """
    board = create_board()
    if solve(board):
        return board
    else:
        raise Exception("盤面の生成に失敗してしまった。。")

def remove_numbers(board, removals=40):
    """
    盤面完全体からランダムに空を作成し、ゲーム化する
    """
    puzzle_board = copy.deepcopy(board)
    count = removals
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle_board[row][col] != 0:
            puzzle_board[row][col] = 0
            count -= 1
    return puzzle_board

def main():
    complete_board = generate_complete_board()
    puzzle_board = remove_numbers(complete_board, removals=40)
    # board = generate_complete_board()
    print("正解盤")
    print_board(complete_board)
    print("[さぁ、解いてみて！]")
    print_board(puzzle_board)

if __name__ == "__main__":
    main()
