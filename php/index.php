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
