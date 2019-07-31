"""
英文字符的鲁棒输入
描述
获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
"""
s = input()
for i in s:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        print(i,end="")