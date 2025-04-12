FROM openjdk:21-bookworm

WORKDIR /app
COPY . .

RUN javac Main.java

# Main クラスがエントリーポイントの場合の実行コマンド
CMD ["java", "Main"]
