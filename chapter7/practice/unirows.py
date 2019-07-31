"""
文件独特行数
描述
统计附件文件中与其他任何其他行都不同的行的数量，即独特行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬


"""
with open("latex.log","r") as f:
    s = f.readlines()

d={}
for line in s:
    d[line]=d.get(line,0)+1

uni=[k for k,v in d.items() if v<=1]
print("共{}独特行".format(len(uni)))
