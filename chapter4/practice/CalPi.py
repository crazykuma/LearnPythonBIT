"""
实例6：圆周率的计算
描述
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，根据在1/4圆内点的数量占总撒点数的比例计算圆周率值。
请以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。
"""
import random
random.seed(123)
Darts = eval(input())
hits = 0
def one():
    x, y = random.random(),random.random()
    if x**2+y**2<=1:
        return 1
    else:
        return 0

for i in range(Darts):
    hits+=one()

pi = 4*(hits/Darts)
print("{:.6f}".format(pi))