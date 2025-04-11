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

//ルールチェック
function isValid($board, $row, $col, $num) {
    for ($j = 0; $j < 9; $j++) {
        if ($board[$row][$j] == $num) {
            return false;
        }
    }
    for ($i = 0; $i < 9; $i++) {
        if ($board[$i][$col] == $num) {
            return false;
        }
    }
    $startRow = $row -($row % 3);
    $startCol = $col -($col % 3);
    for ($i = 0; $i < 3; $i++) {
        for ($j = 0; $j < 3; $j++) {
            if ($board[$startRow + $i][$startCol + $j] == $num) {
                return false;
            }
        }
    }
    return true;
}

//盤面を完成させる。
function solve(&$board) {
    $row = 0;
    $col = 0;
    if (!findEmptyLocation($board, $row, $col)) {
        return true;
    }
    $numbers = range(1, 9);
    shuffle($numbers);
    foreach ($numbers as $num) {
        if (isValid($board, $row, $col, $num)) {
            $board[$row][$col] = $num;
            if (solve($board)) {
                return true;
            }
            $board[$row][$col] = 0;
        }
    }
    return false;
}