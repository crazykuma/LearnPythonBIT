"""
天天向上的力量
问题2：5‰和1%的力量
"""
dayfactor = 0.005
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上：{:.2f}，向下：{:.2f}".format(dayup,daydown))
# 0.005时输出：向上：6.17，向下：0.16
# 0.01时输出：向上：37.78，向下：0.03