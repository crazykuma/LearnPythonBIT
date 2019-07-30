from random import random
from time import perf_counter
DARTS = 1000*1000 # 撒点次数
hits = 0.0        # 命中次数
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()    # 0，1之间的随机坐标
    dist = pow(x**2+y**2,0.5)  # 到圆心的距离
    if dist <=1.0:             # 半径为1，落点到圆心的距离小于半径时为有效命中
        hits = hits+1

pi = 4*(hits/DARTS)            
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}".format(perf_counter()-start))