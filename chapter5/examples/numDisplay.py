"""
七段数码管绘制
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
        date {str} -- ['%Y-%M=%D+']
    """
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年', font=('Arial', 18, 'normal'))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月", font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    # drawDate('20181010')
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


##########################
main()
