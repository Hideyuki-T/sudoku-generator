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