"""
实例8：科赫雪花小包裹
描述
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

科赫曲线，也叫雪花曲线。绘制科赫曲线。
请补充编程模板中代码，完成功能：获得用户输入的整数N，作为阶，绘制N阶科赫曲线。
"""
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3, n-1)

def main(level):
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400,level)
    
try:
    level = eval(input("请输入科赫曲线的阶: "))
    main(level)
except:
    print("输入错误")