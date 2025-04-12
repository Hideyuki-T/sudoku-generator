#!/usr/bin/env python3
# app.py

from flask import Flask, render_template
import sudoku_generator

app = Flask(__name__)

@app.route("/")
def index():
    # 完全盤を生成し、その後でパズル盤を作成
    complete_board = sudoku_generator.generate_complete_board()
    puzzle_board = sudoku_generator.remove_numbers(complete_board, removals=40)
    # 生成結果をテンプレートに渡す
    return render_template("index.html",
                           complete_board=complete_board,
                           puzzle_board=puzzle_board)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

