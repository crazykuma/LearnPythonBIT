"""温度转换
摄氏度：中国等世界大多数国家使用
华氏度：美国、英国等国家使用
转换公式：
C = (F-32) / 1.8
F = C*1.8 + 32
"""
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[:-1])-32)/1.8    #用eval不安全
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")