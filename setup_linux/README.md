# Linuxのセットアップ  
いい加減一人できるようになろうね  

マシンによってはすでに入ってたりするものもあるかも。以下はAWSでubuntu16.04のインスタンスを作成した場合のセットアップです。  

## 目次  
1. tmuxのカスタマイズ  
2. pipの導入  
3. neovimの導入  
4. gitの導入  
5. jupyter notebookの導入  
6. kawaii-termの導入  
7. goofysの導入  
8. JDK8の導入  
9. LightGBMの導入  

## 1. tmuxのカスタマイズ  
参考URL： [tmuxの設定](https://gink03.github.io/tmux/)  
.tmux.confを作成し、上記サイトの「簡易設定」をコピーする。  

## 2. pipの導入  
参考URL: [Ubuntuにpip/pip3をインストールする](http://pcl.solima.net/pyblog/archives/57)  
上から順にコマンド打てばOK  

## 3. neovimの導入  
参考URL：　[neovim設定](https://gink03.github.io/neovim/)  
- 参考URLのinit.vimのリンク先がなんかおかしいので、[ここ](https://bitbucket.org/nardtree/neovim.conf)に飛んでクローンする。  
- クローンしたら、まず「最低限のインストール」を実施。  
- その後、~/.confディレクトリを作成し、neovim.confの中身をコピーする。  
- nvimディレクトリ内のinit.vimに「set terminalguicolor」とあるが、画面が真っ黒になるなどのバグが発生する可能性がある。バグったらコメントアウトor削除。(ただ今回セットアップした時は、この設定はなかったです)  
- a.txtとかa.pyをtouchコマンドで作成してからnvimで開いたらうまく動いた。(関係ないとは思うけど)  

## 4. gitの導入  
git入ってた  
今度記載します  

## 5. jupyter notebookの導入  
参考URL：　[jupyter-dotfiles](https://github.com/GINK03/jupyter-dotfiles) [Jupyter事始め](https://qiita.com/taka4sato/items/2c3397ff34c440044978)  

- まず、「$ sudo pip3 install jupyter」を実行してインストール  
- .jupyterフォルダを作成し、上記リポジトリの.jupyterフォルダの中身を配置する  
- jupyter_notebook_config.pyに記載する、jupyterを使用する際のパスワードのハッシュ値を以下のコマンドで作成  
```
$ python3 -c "import IPython;print(IPython.lib.passwd())"
```
- 表示されたハッシュ値をコピーして、jupyter_notebook_config.pyとjupyter_notebook_config.jsonに反映させる  

- これでjupyterの設定はOK、ただ、クラウド側でアクセスが制限されている可能性があるので、解除する。(AWSだと、自分のEC2に紐づいているセキュリティグループの「インバウンド接続にルールを追加する。具体的には、「全てのIP」から(0.0.0.0/0)、「TCP」で「ポート8888」を許可する。)  

## 6. kawaii-termの導入  
自分用にカスタマイズしたやつをブランチに上げてから導入します  
乞うご期待  

## 7. goofysの導入  
参考URL：[goofys setup and how to use it](https://gink03.github.io/goofys/)  
AWSのS3をマウントする予定があるなら入れる。    

## 8. JDK8の導入  
以下のコマンドを実行。(DebianもUbuntuも共通)  
```
Debian
$ sudo apt install openjdk-8-jdk
Ubuntu
$ sudo apt-get install openjdk-8-jdk  
```

## 9. LightGBMの導入(CPU版)  
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
コンパイルする  
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





