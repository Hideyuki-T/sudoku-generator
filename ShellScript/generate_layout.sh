#!/opt/homebrew/bin/bash

set -euo pipefail

cd ..

# ======= 各言語用ディレクトリと、主要なファイルを定義 =======
declare -A projects=(
  ["python"]="main.py"
  ["java"]="Main.java"
  ["cpp"]="main.cpp"
  ["javascript"]="main.js"
  ["php"]="index.php"
  ["ruby"]="main.rb"
)

for dir in "${!projects[@]}"; do
    mkdir -p "$dir"
    touch "$dir/${projects[$dir]}"
done

# ======= 各言語固有の追加ファイル・ディレクトリの作成 =======
# cpp

# java

# javascript

# php

# python
touch python/app.py
touch python/sudoku_generator.py
mkdir -p python/templates
touch python/templates/index.html

# ruby