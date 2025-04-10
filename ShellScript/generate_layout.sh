#!/opt/homebrew/bin/bash

set -euo pipefail

cd ..

# ======= ディレクトリとファイルの作成 =======
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
