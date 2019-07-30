"""
天天向上的力量
问题3：工作日的力量
一年365天，一周5个工作日，每天进步1%
一年365天，一周2个休息日，每天退步1%
"""
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)

print("工作日的力量：{:.2f}".format(dayup))
# output: 工作日的力量：4.63