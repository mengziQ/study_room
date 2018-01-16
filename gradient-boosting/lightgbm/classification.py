# https://qiita.com/TomokIshii/items/3729c1b9c658cc48b5cb
# https://github.com/Microsoft/LightGBM/tree/master/examples/binary_classification
# scikit-learnをインストールする前に、scipyがあるか確認した方がいい

from sklearn.datasets import load_iris

iris = load_iris()
xs = iris.data
ys = iris.target
