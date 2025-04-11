<?php
//初期化処理
function createBoard() {
    $board = array();
    for ($i = 0; $i < 9; $i++) {
        $row = array();
        for ($j = 0; j < 9; $j++) {
            $row[] = 0;
        }
        $board[] = $row;
    }
    return $board;
}
//盤表示する！
function printBoard($board) {
    foreach ($board as $row) {
        echo implode(" ", array_map(function($num) {
            return ($num === 0 ? "." : $num);
        }, $row)) . "\n";
    }
}

//空セルの座標を返す。
function findEmptyLocation($board, $row, $col) {
    for ($i = 0; $i < 9; $i++) {
        for ($j = 0; $j < 9; $j++) {
            if ($board[$i][$j] === 0) {
                $row = $i;
                $col = $j;
                return true;
            }
        }
    }
    return false;
}