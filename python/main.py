#!/usr/bin/env python3

def create_board():
    """
    9*9の盤面を生成。初期状態は全て０。
    """
    board = [[0 for _ in range(9)] for _ in range (9)]
    return board

def print_board(board):
    """
    盤面を表示する。0は空欄として'.'で表示する。
    """
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def main():
    board = create_board()
    print("初期化された数独のばん面：")
    print_board(board)

if __name__ == "__main__":
    main()
