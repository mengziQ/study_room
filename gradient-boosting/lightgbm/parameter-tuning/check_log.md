## Scikit-learnのfit関数実行ログを見る  
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
