# bundle.pyの仕様  
## メソッドの実行順序  
1. bundle()  
2. 1から呼び出し： _bundle(/ml-treasuredata/result-20170127(ここはtreasuredataの取得状況によって変わる)/part-*')  
3. 2を並列処理(8個のプロセスに分散して実行)

## 2._bundle(arr)の処理内容  
1. misc/conversion.urlsからURLを取り出し、重複を削除
2. /ml-treasuredata/result-20170127内のファイル(part-****)を一つずつ読み込んで(以下)を処理  
3. part-****を一行ずつ読み込んで(以下)を処理  
一行のイメージ  
```
00001af4-bcef-4c48-9ad4-f1f8a56f8141_10493  {"2017-07-03 12:50:53": [null, "http://www.xxxx.com/brand/childcare/?wapr=5959bf18", "www.xxxx.com", 10493, 1005, 1103]}
```
4. 3-1の両端から空白を削除し、keyとvalueに分け、**keyをtuuidとする。**  
tuuidのイメージ  
```
00001af4-bcef-4c48-9ad4-f1f8a56f8141_10493
```
5. valueを細かく分ける  
