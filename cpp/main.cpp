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