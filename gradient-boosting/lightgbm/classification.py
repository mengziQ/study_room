# https://qiita.com/TomokIshii/items/3729c1b9c658cc48b5cb
# https://github.com/Microsoft/LightGBM/tree/master/examples/binary_classification
# scikit-learnをインストールする前に、scipyがあるか確認した方がいい

from sklearn.datasets import load_iris
# cross_validationはそのうち廃止されるので使わない
from sklearn.model_selection import train_test_split
import lightgbm as lgb

iris = load_iris()
X = iris.data
y = iris.target

# random_stateとは、乱数の初期値。指定することで、毎回同じ乱数が生成される。つまり何回試行しても同じデータが学習・テストに使用される。
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=0)

lgb_train =  lgb.Dataset(X_train, y_train)
lgb_evel = lgb.Dataset(X_test, y_test, reference=lgb_train)

# LightGBM parameters
params = {
  'task':'train'
  'boosting_type':'gbdt'
  'objective':'multiclass'
  'metric':
  'num_class':
  'learning_rate':
  'num_leaves':
  'min_data_in_leaf':
  'num_iteration':
  'vervose':
}
