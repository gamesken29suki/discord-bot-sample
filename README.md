# Discord Bot Sample

## 概要
このリポジトリは、Python + discord.py（ver.2.x）で動作するサンプルのDiscord Botです。
- スラッシュコマンド対応
- /hello・/omikuji・/add など、さまざまなコマンドを搭載
- Wikiも御覧ください

## 機能リスト
- `/hello`　… あいさつ
- `/omikuji`　… おみくじ結果を表示
- `/greet [名前]`　… 好きな名前であいさつ
- `/add [a] [b]`　… 2つの数字を足す
- `/coin`　… コイントス
- `/randcolor`　… ランダムカラーコード
- `/today`　… 今日の日付
- `/members` … サーバーメンバー数表示
- `/help` … コマンド一覧（自動生成！）
- `/secret` … 特定ロール限定コマンド（例: 管理者）

## 動作環境・前提
- Python 3.8 以上
- discord.py 2.x 系
- dotenv (pip install python-dotenv)

## セットアップ方法

1. Botアカウントを[Discord Developer Portal](https://discord.com/developers/applications)で取得し、Bot Tokenを取得
2. プロジェクト直下に`.env`ファイルを作成、以下のように記述
    ```
    DISCORD_BOT_TOKEN=あなたのBotトークン
    ```
3. 必要なパッケージをインストール
    ```
    pip install -U discord.py python-dotenv
    ```
4. Botをサーバーに招待（"Send Messages"、"Use Slash Commands"権限に注意）

5. 以下でBotを起動
    ```
    python bot.py
    ```

## 開発Tips
- `.env`は**絶対にGit管理から除外**（.gitignoreに設定済み）
- コマンド一覧ヘルプは自動生成
- チーム開発時はREADMEやIssuesを積極活用！

## 貢献方法
1. 本リポジトリをFork
2. 新規ブランチで機能追加/修正
3. git commit & push
4. Pull Requestを投げる

## ライセンス
MIT

---

