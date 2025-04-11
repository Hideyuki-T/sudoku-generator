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

