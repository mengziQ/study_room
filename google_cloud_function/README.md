# Google Cloud Functionを使う  
参考レポジトリ：[google-cloud-function-pythonic](https://github.com/GINK03/google-cloud-function-pythonic)  
仕事で、EC2を定期的にシャットダウンするためにGoogle Cloud FunctionとLambdaを使いました。  
なんでGoogleCloud Function使ったんだろう？笑  

## 仕組み その１「定期実行」  
lambdaでGCFを起動させて、GCFでEC2をシャットダウンする。  
元々はGCFだけで実装予定だったけど、定期実行の仕組みがGCFになかったっぽいので、GCFの起動のためだけにlambda関数を作成した。  

## 実装でハマったポイント  
- GCPではDebianのインスタンスを作成して、そこで上記作業をしていたが、pypyがうまく動かなかった。ubuntu(yuri)で動かしたら動いた。  
- AWSのIAMユーザーにアタッチするポリシーは「AWSAdmin」でないと動かない。  
- Lambda関数の関数コードはzipファイルをアップロードしたが、この時、zipファイルの作成方法が特殊。ディレクトリごと圧縮してはいけない。aws_lambda_driverの中身のみを圧縮する。コマンドは以下のイメージ。  
```
$ cd aws_lambda_driver
$ zip -r ../aws_lambda_driver .
```

## 仕組み その2「スマホのショートカットから実行」  
乞うご期待  
