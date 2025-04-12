FROM python:3.9-slim

WORKDIR /app
# 必要なら requirements.txt を用いて pip install を行う。。
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# 簡易的に Flask をインストール
RUN pip install --no-cache-dir --default-timeout=100 Flask

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
