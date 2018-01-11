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
8. JDK8の導入(※Debianバージョンもあり！)  

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
参考URL：[Debian系Linuxへ
Oracle JDKをインストールする](http://astah.change-vision.com/ja/feature/install-linux-debian.html)  

### 8-1. Debian GNUでの導入方法  
GCPのVMがDebian GNUだったので、Debianでの方法も調べた。(ubuntuと同じかも)    
作業環境： Debian GNU 9.2  

1. bit数を確認  
```
$ uname -m
```
2. 64bitだったので、JDKのファイルをインストールしてくる。本来はwebサイト上からoracleのライセンス同意しなければならないが、クッキーに「ライセンス同意」の情報を持たせることで、wgetコマンドで直接ダウンロード可能のようです。[Linuxでjdkをwgetする方法](https://qiita.com/hajimeni/items/67d9e9b0d169bf68d1c9)  
```
$ wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz
```
