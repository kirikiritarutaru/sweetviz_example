# sweetviz_example
[sweetviz](https://github.com/fbdesignpro/sweetviz)お試し用リポジトリ

- sweetvizの特徴
  - 探索的データ解析を加速させる高品質な可視化
  - たった2行で実行可能
  - 単独で配布可能なHTMLアプリとして出力可能

- sweetvizの主な関数
  - `analyze()`
    - データフレームに対するEDAの実行
  - `compare()`
    - データフレーム間の比較
  - `compare_intra()`
    - データフレーム内の比較

- 【注意】日本語を含むデータを分析する場合
  - CJKの文字を扱う時は、フォントはNoto Sans CJK JP にする
    1. Noto Sans CJK フォントのインストール
    2. 設定ファイルの作成が必要
      - `sweetviz_setting.ini`を作成し、
        ```
        [General]
        use_cjk_font = 1
        ```

## 参考資料
- [探索的データ解析（EDA）のためのsweetvizを試してみた](https://qiita.com/DS27/items/178416f5ccf3a86db4e6)
- [Sweetvizライブラリによる探索的データ解析](https://mana.bi/wiki.cgi?page=Sweetviz%A5%E9%A5%A4%A5%D6%A5%E9%A5%EA%A4%CB%A4%E8%A4%EB%C3%B5%BA%F7%C5%AA%A5%C7%A1%BC%A5%BF%B2%F2%C0%CF)

## TODO
- bostonデータセットのロード方法を変更
- sweetvizの見かたについて自分メモ作成

