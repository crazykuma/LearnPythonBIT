"""
实例7：七段数码管绘制
 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

描述
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

七段数码管是一种展示数字的有效方式。

请用程序绘制当前系统时间对应的七段数码管，效果如下：       ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

 ‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

要求如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

(1) 使用 time 库获得系统当前时间，格式如下：20190411‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

(2) 绘制对应的七段数码管‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

(3) 数码管风格不限‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

请在本机编写代码完成实例，建议有趣的风格请在Python123的绘图专区上传展示。
"""
import time
import turtle


def drawLine(draw):
    """绘制单段数码管

    Arguments:
        draw {bool} -- [1 for draw,0 for not]
    """
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawDigit(digit):
    """绘制七段数码管

    Arguments:
        digit {Num} -- [0,1,2,3,4,5,6,7,8,9]
    """
    drawLine(1) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(0)
    drawLine(1) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(0)
    drawLine(1) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(0)
    drawLine(1) if digit in [0, 2, 6, 8] else drawLine(0)
    turtle.left(90)
    drawLine(1) if digit in [0, 4, 5, 6, 8, 9] else drawLine(0)
    drawLine(1) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(0)
    drawLine(1) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(0)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    """绘制要输出的日期数字

    Arguments:
        date {str} -- '%Y%m%d'
    """
    turtle.pencolor('red')
    for i in date:
        drawDigit(int(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    # drawDate('20181010')
    drawDate(time.strftime('%Y%m%d', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


##########################
main()