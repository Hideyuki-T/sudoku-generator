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
