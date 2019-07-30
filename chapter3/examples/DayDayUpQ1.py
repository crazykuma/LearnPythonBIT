"""
天天向上的力量
1‰的力量
"""
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))
# output 向上：1.44，向下：0.69
