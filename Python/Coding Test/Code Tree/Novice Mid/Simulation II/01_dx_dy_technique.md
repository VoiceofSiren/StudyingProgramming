# dx dy Technique
###### Question: [https://www.codetree.ai/missions/5/problems/come-back/description](https://www.codetree.ai/missions/5/problems/come-back?&utm_source=clipboard&utm_medium=text)
<br/>

### 이 글의 목적
    - dx dy Technique를 활용하여 문제를 풀어볼 것이다.
    - 저작권법 및 기타 법률에 의하여 필자가 작성한 코드만 공유할 수 있다.
<br/>


#### [코드 1]
```python
n = int(input())
x, y = 0, 0
#     W  S   N  E
dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

dirDict = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3
}

def if_comeback(x, y):
    return x == 0 and y == 0

answer = 0
for i in range(n):
    inputCommand = input().split()
    direction, distance = inputCommand[0], int(inputCommand[1])
    dir_num = dirDict[direction]
    for j in range(distance):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        answer += 1
        if if_comeback(x, y):
            break

#answer = if_comeback(x, y) and answer or -1
print(answer)
```

https://www.codetree.ai/missions/5/problems/come-back?&utm_source=clipboard&utm_medium=text
