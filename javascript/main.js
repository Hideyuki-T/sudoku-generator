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

//ルールチェック
function isValid(board, row, col, num) {
    for (let j =0; j < 9; j++) {
        if (board[row][j] === num) {
            return false;
        }
    }
    for (let i = 0; i < 9; i++) {
        if (board[i][col] === num) {
            return false;
        }
    }
    let startRow = row - (row % 3);
    let startCol = col - (col % 3);
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[startRow + i][startCol + j] === num) {
                return false;
            }
        }
    }
    return true;
}

//完全盤生成
function solve(board) {
    let emptySpot = findEmptyLocation(board);
    if (!emptySpot) {
        return true;
    }
    let [row, col] = emptySpot;

    let numbers = [...Array(9).keys()].map(x => x + 1);
    numbers.sort(() => Math.random() - 0.5); //シャッフル

    for (let num of numbers) {
        if (isValid(board, row, col, num)) {
            board[row][col] = num;
            if (solve(board)) {
                return true;
            }
            board[row][col] = 0;
        }
    }
    return false;
}

//完全盤生成ユーティリティ
function generateCompleteBoard() {
    let board = createBoard();
    if (solve(board)) {
        return board;
    } else {
        throw new Error("盤生成ミスってしまったよ( ͒ •·̫• ͒)˘")
    }
}

//パズル化
function removeNumbers(board, removals) {
    let puzzleBoard = board.map(row => row.slice()); //ディープコピー
    let count = removals;
    while (count > 0) {
        let row = Math.floor(Math.random() * 9);
        let col = Math.floor(Math.random() * 9);
        if (puzzleBoard[row][col] !== 0) {
            puzzleBoard[row][col] = 0;
            count--;
        }
    }
    return puzzleBoard;
}

//結合テスト
function main() {
    try {
        let completeBoard = generateCompleteBoard();
        console.log("完全盤だよ！₍ᐢ..ᐢ₎⊹");
        printBoard(completeBoard);

        let puzzleBoard = removeNumbers(completeBoard, 40);
        console.log("\nさぁ解いてみて！");
        printBoard(puzzleBoard);
    } catch (error) {
        console.error("エラ〜〜〜〜〜〜：", error.message);
    }
}

main();