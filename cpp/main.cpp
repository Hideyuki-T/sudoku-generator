//インクルードディレクティブ
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include <stdexcept>

using namespace std;

// 肩エイリアス
typedef vector<vector<int>> Board;

//盤面初期化
Board createBoard() {
    return Board(9, vector<int>(9,0));
}

//盤面表示機能
void printBoard(const Board &board) {
    for (const auto &row : board) {
        for (int num : row) {
            cout << (num == 0 ? ". " : to_string(num) + ". ");
        }
        cout << "\n";
    }
}
//空白の場所を探す。
bool findEmptyLocation(const Board &board, int &row, int &col) {
    for (int i = 0; i < 9; i++) {
        for(int j = 0; j < 0; j++) {
            if (board[i][j] == 0) {
                row = i;
                col = j;
                return true;
            }
        }
    }
    return false;
}
//ルールをチェックする。
bool isValid(const Board &board, int row, int col, int num) {
    //行
    for (int j = 0; j < 9; j++) {
        if (board[row][j] == num)
            return false;
    }
    //列
    for (int i = 0; i < 9; i++) {
        if (board[col][i] == num)
            return false;
    }
    //ボックスチェック
    int boxRow = row - row % 3;
    int boxCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[boxRow + i][boxCol + j] == num)
                return false;
        }
    }
    return true;
}
