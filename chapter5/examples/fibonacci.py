"""
斐波那契数列
F(n)当n=1或n=2时，F(n)=1
其他情况F(n)=F(n-1)+F(n-2)
"""
def febonacci(n):
    if n in [1,2]:
        return 1
    else:
        return febonacci(n-1)+febonacci(n-2)

# 1,1,2,3,5,8,13,21,34,55
print(febonacci(10))


