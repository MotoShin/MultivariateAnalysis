import sys
import numpy as np
import matplotlib.pyplot as plt

def calculation_covariance(x, y):
    xy = x * y
    mu_xy = np.mean(xy)
    mu_x = np.mean(x)
    mu_y = np.mean(y)
    return mu_xy - mu_x * mu_y

def least_square_method(x, y):
    mu_x = np.mean(x) # x の平均
    mu_y = np.mean(y) # y の平均    
    variance = np.var(x) # 分散
    covariance = calculation_covariance(x, y) # 共分散

    a = covariance / variance
    b = -1 * a * mu_x + mu_y

    return a, b

def u(a, b, x):
    return a*x+b

def main():
    args = sys.argv
    datas = np.loadtxt(args[1], delimiter=",")

    print(datas)

    x = datas[0]
    y = datas[1]

    a, b = least_square_method(x, y)

    print("a: {}, b: {}".format(a, b))

    fig = plt.figure() # Figureオブジェクトを作成
    ax = fig.add_subplot(1,1,1) # figに属するAxesオブジェクトを作成
    ax.plot(x, u(a, b, x), 'k')
    ax.plot(x, y, 'o')
    plt.show()

main()
