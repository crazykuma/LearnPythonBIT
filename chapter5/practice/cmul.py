"""
任意累积

描述
请根据编程模板补充代码，计算任意个输入数字的乘积。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

注意，仅需要在标注...的地方补充一行或多行代码。
def cmul(...):
    ...

print(eval("cmul({})".format(input())))
"""

def cmul(*num_list):
    m=1
    for i in num_list:
        m*=i
    return m

print(eval("cmul({})".format(input())))