# プロセス・サブプロセスの生成  
参考コード [yahoo_operation_range.py](https://github.com/GINK03/StormRuler/blob/master/bin/yahoo_operation_range.py)  
仕事でRESTインターフェースを持つ外部サービスを利用する機会がありました。  
参考にしたコードがhttp接続するときに、「os.popen」を使用しており、それが何をやっているのかイマイチ理解できていません。  
 
[このサイト](http://takuya-1st.hatenablog.jp/entry/2016/04/11/044313)が分かりやすいかも？  

## 分かったこと    
- callとPopenは子プロセス生成してコマンドを実行するかしないかの違い。callは子プロセスを作らない。なのでpythonからコマンドが実行されたことになり、コマンドが終了するまでpythonスクリプトも実行が終わらない。  
- os.popenとsubprocessモジュールのPopenは、前者がshell経由でコマンド実行され、後者はshellパラメーターで指定しない限りshellを経由しない。

## 実装でハマったポイント  
shell経由しない場合、コマンドの渡し方がよく分からない。配列にしないといけないようだけど、splitで配列にしてもうまくいかない。今度考えます。。  
