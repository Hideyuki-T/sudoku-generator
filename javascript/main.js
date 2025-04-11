//盤面初期化
function createBoard() {
    let board = new Array(9).fill(0).map(() => new Array(9).fill(0));
    return board;
}

//盤面表示
function printBoard(board) {
    board.forEach(row => {
        console.log(row.map(num => (num === 0 ? '.' : num)).join(' '));
    });
}

//空セル検出
function findEmptyLocation(board) {
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (board[i][j] === 0) {
                return [i, j];
            }
        }
    }
    return null;
}