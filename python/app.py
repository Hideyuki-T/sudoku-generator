#!/usr/bin/env python3
# app.py

from flask import Flask, render_template
import sudoku_generator

app = Flask(__name__)

@app.route("/")
def index():
    complete_board = sudoku_generator.generate_complete_board()
    puzzle_board = sudoku_generator.remove_numbers(complete_board, removals=40)
    return render_template("index.html", complete_board=complete_board, puzzle_board=puzzle_board)

if __name__ == "__main__":
    app.run(debug=True)
