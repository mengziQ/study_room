## パラメーターのチューニング手順  
scikit-learnのGridSearchCVでgrid paramsを指定します。  
このとき、チューニングしたいパラメータを一気に指定してもいいのですが、特徴量やデータ量が多いとチューニングに時間がかかります。  
なので、パラメータを小分けにしてチューニングしていきます。  

パラメーターチューニングには効率が良いとされる順番があるようです。[このサイト](http://kamonohashiperry.com/archives/209)によると、以下の順番でチューニングするのが良いそうです。  

1. 学習率と木の数  
2. 木に関するパラメーター：　max_depth, min_child_weight, gamma, subsample, colsample_bytree
3. 正則化パラメータ: lambda, alphaなど  
4. 学習率を下げる  

## Scikit-learn GridSearchCVのfit関数実行ログを見る  
verbose=3にすると以下のログが出力される
```
Fitting 4 folds for each of 1728 candidates, totalling 6912 fits
[CV] subsample=0.7, reg_lambda=1, boosting_type=gbdt, n_estimators=1000, learning_rate=0.06, random_state=501, reg_alpha=1, num_leaves=31, objective=regression, colsample_bytree=0.7 
[CV]  subsample=0.7, reg_lambda=1, boosting_type=gbdt, n_estimators=1000, learning_rate=0.06, random_state=501, reg_alpha=1, num_leaves=31, objective=regression, colsample_bytree=0.7, score=0.9975824977932051, total=  16.1s
[Parallel(n_jobs=1)]: Done   1 out of   1 | elapsed:   24.0s remaining:    0.0s
[CV] subsample=0.7, reg_lambda=1, boosting_type=gbdt, n_estimators=1000, learning_rate=0.06, random_state=501, reg_alpha=1, num_leaves=31, objective=regression, colsample_bytree=0.7 
[CV]  subsample=0.7, reg_lambda=1, boosting_type=gbdt, n_estimators=1000, learning_rate=0.06, random_state=501, reg_alpha=1, num_leaves=31, objective=regression, colsample_bytree=0.7, score=0.9979117721237265, total=  16.5s
[Parallel(n_jobs=1)]: Done   2 out of   2 | elapsed:   48.5s remaining:    0.0s
[CV] subsample=0.7, reg_lambda=1, boosting_type=gbdt, n_estimators=1000, learning_rate=0.06, random_state=501, reg_alpha=1, num_leaves=31, objective=regression, colsample_bytree=0.7 
[CV]  subsample=0.7, reg_lambda=1, boosting_type=gbdt, n_estimators=1000, learning_rate=0.06, random_state=501, reg_alpha=1, num_leaves=31, objective=regression, colsample_bytree=0.7, score=0.9981020341201355, total=  16.5s
・・・
```
### 実行時間の見積  
totalling fitsの回数と、1回の交差検証のtotalの秒数を見ることで分かる。  
上記の例であれば、
```
6912　×　約16秒 = 110592秒 = 30.72時間  
```
