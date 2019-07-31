"""
文件行数
描述
打印输出附件文件的有效行数，注意：空行不计算为有效行数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

输入输出示例
这是仅给出输出格式样例，不是结果。
"""
with open("latex.log",'r') as f:
    s=f.readlines()

count=0
null_count=0
for line in s:
    line = line.strip("\n")
    if len(line)!=0:
        count+=1
    
print("共{}行".format(count))