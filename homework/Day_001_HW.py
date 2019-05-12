#!/usr/bin/env python
# coding: utf-8

# ## 練習時間
# #### 請寫一個函式用來計算 Mean Square Error
# $ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $
# 
# ### Hint: [如何取平方](https://googoodesign.gitbooks.io/-ezpython/unit-1.html)

import numpy as np
import matplotlib.pyplot as plt
"""
def mean_squared_error(a, b): #相減, 取平方, 取平均
    temp = 0
    for i in range(len(a)):
        temp += (a[i] - b[i]) **2
    avg = temp / len(a)
    return avg    

def mean_absolute_error(a, b): #abs(相減), 取平均
    temp = 0
    for i in range(len(b)):
        temp += (abs(a[i] - b[i]))
    avg = temp / len(b)
    return avg
"""

def mean_squared_error(a, b):
    avg = np.mean((a - b) **2)
    return avg

def mean_absolute_error(a, b):
    avg = np.mean(np.abs(a - b))
    return avg

w = 3
b = 0.5

x_lin = np.linspace(0, 100, 101) 
#print(type(x_lin))
y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()

y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))

