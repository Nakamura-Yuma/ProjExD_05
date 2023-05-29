# ゲームのタイトル 
Run on fence
## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
 主人公キャラクター(棒人間)を方向キー操作により障害物を避けるゲームで、様々な能力を駆使してなるべく多くの距離を走ることを目指すゲーム。

## ゲームの実装
### 共通基本機能
* 主人公キャラクターに関するクラス:playerクラス
* 障害物に関するクラス:objectクラス

## 操作方法
* スペースキーでジャンプ
* 下キーでスライディング(追加機能)

## クリア方法
* 現時点でなし
* キャラクターが障害物に衝突することで終了

## 担当追加機能
* スライディング機能の追加
* 障害物2の追加

### ToDo
 - [ ] スライディング機能
 - [ ] DOWNキーを押したらスライディングする
 - [ ] 空中の障害物(障害物2)の追加

### メモ
* スライディング機能はPlayerクラスに追加しました
* Object2クラスは障害物2を表示するクラスです