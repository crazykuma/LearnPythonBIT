"""
汉诺塔
补充：
汉诺塔的游戏思路其实就是怎么把大象关进冰箱：
1：打开冰箱的门（移动n-1个盘子到临时位）
2：把大象塞进去（把第n个盘子塞到目标位）
3：把门关上（移动n-1个盘子从临时位到目标位)
"""
count = 0
def hanoi(n,src,dst,mid):
    """汉诺塔
    
    Arguments:
        n {int} -- num of plates
        src {str} -- start node
        dst {str} -- target node
        mid {str} -- temp node
    """
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count+=1
        hanoi(n-1,mid,dst,src)

hanoi(3,"A","C","B")