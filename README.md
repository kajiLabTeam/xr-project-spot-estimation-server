# スポット推定サーバ
## 実行方法
### DBコンテナの立ち上げ
```bash
make up
```
### モジュールインストール
`pipenv`が入っていない場合
```bash
brew install pipenv
```

```bash
pipenv install
```

### 仮想環境にログイン
```bash
pipenv shell
```

### サーバの実行
```bash
cd src # main.pyが存在するディレクトリ移動

uvicorn main:app --host 0.0.0.0 --port 80 --reload # エントリーポイントを実行
```

## その他
### DBコンテナに入りたいとき
```bash
make db
```
