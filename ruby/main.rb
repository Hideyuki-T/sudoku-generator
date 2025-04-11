//盤面初期化
def create_board
    Array.new(9) {Array.new(9, 0) }
end

//盤面表示
def print_board(board)
    board.each do |row|
        puts row.map { |num| num == 0 ? '.' : num.to_s }.join(" ")
    end
end

//空セル検出
def find_empty(board)
    board.each_with_index do |row, i|
      row.each_with_index do |num, j|
        return [i, j] if num == 0
      end
    end
    nil
end

//ルールチェック
def valid?(board, row, col, num)

    return false if board[row].include?(num)
    return false if board.any? { |r| r[col] == num }

    start_row = row - row % 3
    start_col = col - col % 3
    (start_row...(start_row + 3)).echo do |i|
        (start_col...(start_col + 3)).echo do |j|
            return false if board[i][j] == num
        end
    end
    true
end
