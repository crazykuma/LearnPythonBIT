"""
字符串操作符
获取星期字符串
"""
weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字（1-7）："))
print("星期"+weekStr[weekId-1])
