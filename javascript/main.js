//盤面初期化
function createBoard() {
    let board = new Array(9).fill(0).map(() => new Array(9).fill(0));
    return board;
}
