### 条条大路通罗马
### 这道题的意思是给定两个数组A和B，A中的节点表示出发城市，B的节点表示到达城市
### 找出一个城市，所有的城市都能到达的
### 我的思路是，通过一个哈希表存储A中所有出发城市的作为key，出度数作为value
### 一个罗马城市的特点是，出度为0. 如果存在两个出度为0的城市的话，返回-1，否则返回这个城市
from collections import Counter
def Rome(A, B):
    if not A or not B:
        return -1
    n = len(A)
    counter = Counter(A)

    # for c in A:
    #     out_degree[c] += 1
    
    rome = -1
    print(counter)
    for city in range(n + 1):
        if counter[city] == 0:
            if rome != -1:
                # return -1
                print(-1)
                break
            rome = city
    # return rome 
    print(rome)    
Rome(A = [0, 1, 2, 4, 5], B = [2, 3, 3, 3, 2])
Rome(A = [2, 3, 3, 4], B = [1, 1, 0, 0])