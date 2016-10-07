# svm

## [LinerSVC](liner_SVC.py)
線形なサポートベクターマシン．サンプルではIRIS Datasetsのpetal length,petal widthの二つを抜き取り分類する．
Cを変更することで許容する分類不可なものの侵入距離が変わる

## [SVC](SVC.py)
様々なサポートベクターマシン．サンプルではIRIS Datasetsのpetal length,petal widthの二つを抜き取り分類する．
SVCクラスのkernel変数を変更することで使用するカーネル関数を変えられる（線形もある)．Cを変更することで許容する分類不可なものの侵入距離が変わる
