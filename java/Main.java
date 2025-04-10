import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Main {

    public static void main(String[] args){
    //完全盤作成
    int[][] completeBoard = genelateCompleteBoard();
    System.out.println("完全盤だよ！");
    printBoard(completeBoard);
    //パズル盤にするために４０セルを削除
    int[][] puzzleBoard = removeNumbers(completeBoard, 40);
    System.out.println("さぁ、解いてみて！");
    printBoard(puzzleBoard);
    }

    //盤を初期化
    public static int[][] createBoard(){
        int[][] board = new int[9][9];
        //盤全てを０に設定
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
            board[i][j] = 0;
            }
        }
        return board;
    }
    //盤表示
    public static void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int num : row) {
                System.out.print((num == 0 ? ". " : num + " "));
            }
            System.out.println();
        }
    }
    //空白を探す。なければnull。
    public static int[] findEmptyLocation(int[][] board) {
        for (int i = o; i < 9; i++){
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    return new int[] { i, j };
                }
            }
        }
        return null;
    }
    //ルールに違反しないかチェックする。
    public static boolean isValid(int[][] board, int row, int col, int num) {
        //行をチェック
        for (int j = 0; j < 9, j++){
            if (board[row][j] == num) {
            return false;
            }
        }
        //列をチェックする
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == num) {
                return false;
            }
        }
        //ボックスチェック
        int boxRow = row - row % 3;
        int boxCol = col -col % 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[boxRow + i][boxCol + j] == num) {
                    return false;
                }
            }
        }
        return true;
    }
    //バックトラッキングで盤面解決
    public static boolean solve(int[][] board) {
        int[] empty = findEmptyLocation(board);
        if (empty == null) {
            return true;
        }
        int row = empty[0], col = empty[1];
        //1~9をランダムに試してみて、盤生成を多様化してみる。
        List<Integer> Numbers = new ArrayList<>();
        for (int num = 1; num <= 9; num++) {
            Numbers.add(num);
        }
        Collections.shuffle(numbers);

        for (int num : numbers) {
            if (isValid(board, row, col, num)) {
                board[row][col] = num;
                if (solve(board)){
                    return true;
                }
                board[row][col] = 0;
            }
        }
        return false;
    }
    //盤を完成させる。
    public static int[][] generateCompleteBoard() {
        int[][] board = createBoard();
        if (solve(board)) {
            return board;
        } else {
            throw new RuntimeException("生成に失敗したわ。(人д｀o)ｺﾞﾒﾝﾈ")
        }
    }
    //完全盤からランダムで削除してパズルにする。
    public static int[][] removeNumbers(int[][] board, int removals) {
        int[][] puzzle = copyBoard(board);
        Random rand = new Random();
        int count = removals;
        while (count > 0) {
            int row = rand.nextInt(9);
            int col = rand.nextInt(9);
            if (puzzle[row][col] != 0) {
                puzzle[row][col] = 0;
            }
        }
        return puzzle;
    }
    //盤のディープコピーを作成
    public static int[][] copyBoard(int[][] board) {
        int[][] copy = new int [9][9];
        for (int i = 0; i < 9; i++) {
            copy[i] = board[i].clone();
        }
        return copy;
    }
}
