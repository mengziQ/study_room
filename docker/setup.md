# コンテナの環境設定  
コンテナ内にpythonプログラムを配置している想定で環境設定します。ubuntu想定です。  

## sudoのインストール  
まさかのsudoが入っていませんでした。。。下記のコマンドでエラーを吐く場合はapt-getをupdateします。  
```
$ apt install sudo
```

## pipのインストール→pip3のインストール  
これでpython(3)も入ります。  
```
$ apt-get install python(3)-pip
```

## mecabのインストール  
だいたいmecab使ってること多いよね。  
(https://github.com/mengziQ/study_room/tree/master/setup_linux)参照。  

## その他pipで入れたもの  
- bs4  
- requests  

## あった方が親切？  
- neovim  
- git  
