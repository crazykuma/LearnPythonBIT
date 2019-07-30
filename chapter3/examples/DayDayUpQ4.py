"""
天天向上的力量
问题4：工作日的努力
工作日要努力到什么水平，才能与每天努力1%一样
A君：一年365天，每天进步1%，不停歇
B君：一年365天，每周工作5天休息2天，休息日下降1%，要多努力才能跟A君一样
"""
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup

dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor+=0.001

print("工作日的努力参数是：{:.3f}".format(dayfactor))