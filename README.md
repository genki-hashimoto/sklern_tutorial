# sklern_tutorial
Pythonのscikit-learnパッケージの使い方を日本語でアバウトに書いていく(予定)

## clustering
クラスタリングができる

## svm
サポートベクターマシン(svm)を使える．svmにはマージン内への侵入を許可しないハードsvmと分離不可能な問題のさい学習の際に分類不可となるマージン内にあるデータの存在を認めるソフトsvmがあるが，ハードなsvmのみを実装したものはない．
許容の度合いはパラメータCの大きさに依存するため，大きくすればハードsvmに近づく．
- [SVC]()
	- カーネル関数を用いたsvmによるクラス分類
- [LinerSVC]()
	- 線形svmによるクラス分類
## preprocessing
データの整形などの前処理
- [scale](preprocessing/scale)
	- 正規化関数
