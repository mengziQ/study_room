# http://www.procrasist.com/entry/16-neural-net
import numpy as np

# 入力層・隠れ層・出力層の3層からなる基本的なNN
class NN:
  def __init__(self, num_input, num_hidden, num_output, learning_rate):
    self.num_input = num_input # 入力層のパーセプトロンの数
    self.num_hidden = num_hidden
    self.num_output = num_output
    self.learning_rate = learning_rate

    # 全結合なので、各層のパーセプトロン数の行列が重みとなる
    self.w_input2hidden = np.random.random((self.num_input, self.num_hidden))
    self.w_hidden2output = np.random.random((self.num_hidden, self.num_output))
    # これ何　bって何
    self.b_input2hidden = np.ones((self.num_hidden))
    self.b_hidden2output = np.ones((self.num_output))

  # 隠れ層の活性化関数
  def sigmoid(self, x):
    return(1 / (1 + np.exp(-x)))

  # 活性化関数(シグモイド)の微分
  def dactivate_func(self, x):    
    # これは商の微分公式でふ。シグモイドの微分も参照。
    return(self.sigmoid(x)*(1 - self.sigmoid(x)))

  # 出力層の活性化関数
  def softmax(self, x):
    C = x.max()
    # この式意味分からんなぁ・・・なんでC引くの？ていうか.max()の書き方ってpythonにある？
    return (np.exp(x - C) / np.exp(x - C).sum())

  # 順伝播計算
  def forward_propagation(self, x):
    # 図から考えるとuとzの記号逆じゃないの・・・？
    u_hidden = np.dot(self.w_input2hidden, x) + self.b_input2hidden # 何故か1だけのベクトルを足す
    z_hidden = self.sigmoid(u_hidden)

    u_output = np.dot(self.w_hidden2output, z_hidden) + self.b_hidden2output
    z_output = self.softmax(u_output)
    return u_hidden, z_hidden, u_output, z_output

  # 逆誤差伝搬法
  # まずは出力値から誤差(デルタ)を求める 
  def backward_propagation(self, t, u_hidden, z_output):
    t_vec = np.zeros(len(z_output))
    t_vec[t] = 1
    delta_output = z_output - t_vec # なんで引くんだろう・・・
    delta_hidden = np.dot(delta_output, self.w_hidden2output * self.dactivate_func(u_hidden))
    return delta_hidden, delta_output

  # 重みの勾配を求める
  def calc_gradient(self, delta, z):
    dW = np.zeros((len(delta), len(z)))
    for i in range(len(delta)):
      for j in range(len(z)):
        dW[i][j] = delta[i] * z[j]
    return dW

  # 重みを更新
  def update_weight(self, w0, gradE):
    return w0 - self.learning_rate * gradE

  




  





    



