FROM gcc:latest

WORKDIR /usr/src/app
COPY . .

# main.cpp をコンパイルして、sudoku という実行ファイルを作成
RUN g++ -o sudoku main.cpp

CMD ["./sudoku"]
