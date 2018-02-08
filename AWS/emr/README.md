# EMRで並列分散処理を実施する  
まずはwordcountを体験して、EMRの使い方を覚えます。  

## 0. 事前準備(今回は割愛)  
- mapperとreducerの開発    
- S3バケットの作成、mapper、reducer、分散処理するデータの配置  
- stepのjsonファイルを作成
```
[
  {
     "Name": "WordCount",(クラスターのステップタブで表示される名前)
     "Type": "STREAMING",
     "ActionOnFailure": "CONTINUE",
     "Args": [
         "-files",
         "s3://xxxxx/mapper.py,s3://xxxxx/reducer.py",
         "-mapper",
         "mapper.py",
         "-reducer",
         "reducer.py",
         "-input",
         "s3://yyyyy/",
         "-output",
         "s3://zzzzz"]
  }
]
``` 


## 1. クラスターの作成  
EMRのコンソールから作成する。「クラスターを作成」ボタンをクリック。  

### 変更が必要な箇所  
- 一般設定  
クラスター名：てきとう  

- 詳細オプション設定(「詳細オプションに移動する」をクリック)  
ステップの追加：「最後のステップが完了したらクラスターを自動的に終了します。」にチェック  

## 2. EMR実行  
以下のコマンドを実行する。(※1で作成したクラスターのステータスが「終了済み」になる前に実行しましょう)  
ちなみに、この工程を実施するインスタンスはAWS CLIが入っていて、stepの設定ファイルが置いてあるものならなんでもOKです。GCPでも実行できました。  
```
aws emr add-steps --cluster-id j-xxxxxx --steps file://./WordCount_step.json --region ap-northeast-1
```
- clster: EMRのID
- step   : MapReduceフローを記述したjsonを渡す
- region: EMRの地域  

## 補足：mapperやreducerをデバックしたいとき  
mapperとreducerが置いてあるS3バケットをマウントするなどして、そのディレクトリに移動し、デバックする。  
```
最初のコマンドの出力をパイプで送付することで、次のコマンドの入力とすることができる。
Head -n 3 *gz | python3 maper.py |python3 reducer.py 
```

## 3. エラー確認  
EMRのコンソールで確認。成功していると各種ステータスはこんな感じ。  
※クラスター > ステップ > ジョブ > タスク  

- クラスターのステータス： 終了済み  
- ステップのステータス：　終了済み  
- ジョブ(右にスクロールするとある)の状態： COMPLETED  
- タスク(右n)の状態：COMPLETED  

## 4. 処理結果  
wordcountを実施すると、こんな感じのファイルが出力されました。単語と出現回数が書かれています。  
```
ファイル名：part-00000

thing. 1	
lying 1	
centre 1	
do 3	
walking 1	
certain 1	
roof. 1	
once 3	
Alice; 1	
pleasure 1	
Why, 2	
seldom 1	
lock, 1	
After 1	
eye 1	
take 1	
schoolroom, 1	
grow 2	
・・・・
```
