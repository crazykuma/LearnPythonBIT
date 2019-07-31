"""
实例9：基本统计值计算
描述
这是"实例"题，与课上讲解实例相同，请作答检验学习效果。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

获取以逗号分隔的多个数据输入（输入为一行），计算基本统计值（平均值、标准差、中位数）‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

除中位数外，其他输出保留小数点后两位。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

请补充编程模板中代码完成
"""
def getNum():
    nums = list(eval(input()))
    return nums

def mean(numbers):
    """计算平均值
    
    Arguments:
        numbers {list} -- list object of numbers
    """
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)

def dev(numbers,mean):
    """计算方差
    
    Arguments:
        numbers {list} -- list object of numbers
        mean {float} -- mean value of numbers
    """
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    """计算中位数
    
    Arguments:
        numbers {list} -- list object of numbers
    """
    numbers=sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNum()
m = mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m,dev(n,m),median(n)))