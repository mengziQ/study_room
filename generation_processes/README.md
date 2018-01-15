# プロセス・サブプロセスの生成  
参考コード [yahoo_operation_range.py](https://github.com/GINK03/StormRuler/blob/master/bin/yahoo_operation_range.py)  
仕事でRESTインターフェースを持つ外部サービスを利用する機会がありました。  
参考にしたコードがhttp接続するときに、「os.popen」を使用しており、それが何をやっているのかイマイチ理解できていません。  

公式ドキュメントには、「コマンド cmd への、または cmd からのパイプ入出力を開きます。」とあるのですが、これはコマンドからosにパイプが繋がってコマンドが実行される感じなのでしょうか？  
コマンドを実行するだけならcallメソッドがあって、それとの違いも分かっていません。  
[このサイト](http://takuya-1st.hatenablog.jp/entry/2014/08/23/022031)によると、シェル経由かそうでないかの違いっぽいですが、このpopenはsubprocessモジュールの話です
