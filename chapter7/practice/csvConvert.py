"""
CSV格式列变换
描述
附件是一个CSV文件，请将每行按照列逆序排列后输出，不改变各元素格式（如周围空格布局等）。
"""
with open("data.csv",'r') as f:
    s=f.readlines()

for line in s:
    line = line.strip('\n')
    ls = line.split(',')
    output = ','.join(ls[::-1])
    print(output)

