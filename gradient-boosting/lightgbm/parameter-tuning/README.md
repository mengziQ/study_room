# エラーとその対処法  
## Memory Error  
nthread

## [LightGBM] [Warning] bagging_fraction is set=0.7, subsample=0.8 will be ignored. Current value: bagging_fraction=0.7.   
同じパラメータに対して、Scikit-learnAPIとLightGBMで別のパラメータ名を指定している可能性あり。  
例えば、bagging_fractionはaliasとしてcolsample_bytreeでも指定できる。どちらかに統一する必要がある。  
※Scikit-learnのパラメータはaliasがないので、こちらに統一する。  

## warnings.warn("Found `{}` in params. Will use it instead of argument".format(alias))  
調査中  
