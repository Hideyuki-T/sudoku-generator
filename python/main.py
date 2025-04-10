#!/usr/bin/env python3
import random

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

def main():
    board = generate_complete_board()
    print("[さぁ、解いてみて！]")
    print_board(board)

if __name__ == "__main__":
    main()
