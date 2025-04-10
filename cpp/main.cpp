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
