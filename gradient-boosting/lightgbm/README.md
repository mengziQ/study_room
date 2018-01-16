# LightGBMの導入(CPU版)  
大まかな流れはビルドしてコンパイルして、インストールする。  

LightGBMのレポジトリをクローンする  
```
$ git clone https://github.com/Microsoft/LightGBM.git
```
LightGBMディレクトリに移動し、ビルド用ディレクトリ「build」を作成し、移動する  
```
$ cd LightGBM
$ mkdir build
$ cd build
```
cmakeコマンドがあるか確認  
```
$ which cmake 
```
あったら、LightGBMをビルドする  
```
$ cmake ..
```
コンパイルする(コンパイルを並列処理で実行する)  
```
$ make -j8
$ make -j2 ←こっちの方がいいかも。メモリが足りないとか怒られた。
```
ようやくインストール  
```
$ sudo make install
```
ちゃんと入っているか確認  
```
$ which lightgbm
```
※ちなみに、、、GPUが入っているか確認するコマンド  
```
$ lspci | grep VGA 
```

## パラメーターはここを見よ  
https://github.com/Microsoft/LightGBM/blob/master/docs/Parameters.rst
