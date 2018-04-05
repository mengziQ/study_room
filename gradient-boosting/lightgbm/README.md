# ネット広告のクリエイティブからCTRを予測する  
ネット広告に掲載される画像(クリエイティブ)から、その広告のCTRを予測できないかというモチベーションで実施した分析です。  
クリエイティブをタグ要素に分解し、どのタグがCTRを上昇させているのか・もしくは下降させているのかを調べます。  

## 概要図  
![概要図](https://github.com/mengziQ/study_room/blob/master/gradient-boosting/lightgbm/pics/overview.PNG)

## 使用方法  
**注意**  
すごーく長いです。データ取得〜学習〜予測まで記載しました。  

### 1. Google Adword　APIで入手したクリエイティブとCTR実績値を結合する  
クリエイティブデータとCTR値は社内専用のAPIでGoogle Adwords APIを操作して取得しているためスクリプトは割愛します。  

以下のレポートから取得しています。  
- クリエイティブデータ： MEDIA_SERVICE_WITH_IMAGE(調査中)  
- CTR値： [AD_PERFORMANCE_REPORT](https://developers.google.com/adwords/api/docs/appendix/reports/ad-performance-report)

取得したCTR値(この時点では全てのパフォーマンスデータ)をjson形式に変換し、Ad IDが分かるようなファイル名に変更します。  
```
$ python3 imgs_data.py -perform

```

上で作成したjsonファイル(パフォーマンスデータ)とクリエイティブデータ(配列に変換)をAd IDで結合します。
```
$ python3 imgs_data.py -image
```

### 2. クリエイティブ→画像タグへの変換    
**使用したAPI**  
Google Cloud Vision API  

まず、クリエイティブ画像(画像そのもの)をGoogle Cloud Vision APIに読み込ませるためにリサイズする  
```
入力： クリエイティブ
出力： 縮小or拡大したクリエイティブ画像(一辺が最大224ピクセルとなるようにリサイズ)

$ python3 vision/vision.py --minimize
```

リサイズしたクリエイティブのタグを検出する  
```
入力：　 リサイズしたクリエイティブ
出力：　 画像タグ(json)

$ python3 vision/vision.py --scan
```

### 3. tag_idxの作成  
クリエイティブへのタグ付けが終了したら、全タグを探索してidを振ります。スクリプトどっか消えました。  
この後、諸々作業して精度が悪かったので特徴量を減らしました。その際にタグの出現頻度を調べたので、これが参考になるかもしれません笑  
```
$ python3 tag_freq.py
```

出現頻度を元に特徴量を削減する
```
$ python3 reduce_tag.py
```

最終的なtag_idxはこちら → tag_idx2.pkl


### 4. 画像タグ・実績CTRを結合してSVMファイルを作成    
すごーく分かりづらいのですが、1でできたpickleファイル(パフォーマンスと画像配列)と2でできたjsonファイル(画像タグ)を画像名で照合しつつ、
3で作ったtag_idx2.pklを使ってLightGBMに読み込ませるためのSVMファイルを作成します。  

```
ラベルをCTRにしたいので、以下のように引数に指定してください

$ python3 kpi_tag.py ctr
```

### 5. LightGBMによる学習  
インストール方法は[ここ](https://github.com/mengziQ/study_room/blob/master/gradient-boosting/lightgbm/docs/installation.md)か公式githubを参照ください。  

```
$ cd ctr
$ lightgbm config=train.conf
```

### 6. 予測
```
$ cd ctr
$ lightgbm config=predict.conf
```

### 予測以降の作業工程  


