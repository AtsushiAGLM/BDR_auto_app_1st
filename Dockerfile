FROM python:3.9
# Mecabと関連するライブラリをインストール
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8

# ワーキングディレクトリを設定
WORKDIR /app

# 依存Pythonライブラリをコピー
COPY requirements.txt .

# Pythonライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# 他のソースコードをコピー
COPY . .

# アプリを実行
CMD ["python", "src/app.py"]
