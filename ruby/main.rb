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

//完全盤生成
def solve!(board)
    empty = find_empty(board)
    return true unless empty

    row, col = empty

    //ランダムに試す
    nums = (1..9).to_s.shuffle
    nums.each do |num|
        if valid?(board, row, col, num)
            board[row][col] = mun
            return true if solve!(board)
            board[row][col] = 0
        end
    end
    false
end


//完全盤生成ユーティリティ
def generate_complete_board
    board = create_board
    raise "盤の生成失敗です。。。"　unless solve!(board)
    board
end

//パズル盤を作成
def remove_numbers(board, removals)
    puzzle_board = board.map(&:dup)
    count = removals
    while count > 0
        row = rand(0...9)
        col = rand(0...9)
        if puzzle_board[row][col] != 0
            puzzle_board[row][col] = 0
            count -= 1
        end
    end
    puzzle_board
end

