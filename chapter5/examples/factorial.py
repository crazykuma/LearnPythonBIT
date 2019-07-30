"""
阶乘使用递归实现
"""
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))