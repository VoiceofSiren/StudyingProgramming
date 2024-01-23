# dx dy Technique
###### Question: [https://www.codetree.ai/missions/5/problems/come-back/description](https://www.codetree.ai/missions/5/problems/come-back?&utm_source=clipboard&utm_medium=text)
<br/>

### 이 글의 목적
    - dx dy Technique를 활용하여 문제를 풀어볼 것이다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### 구현 과정 - 1
- 방향에 따른 dx 배열과 dy 배열의 index 값을 맞춰주기 위해 [코드 1-1]에서 dirDict를 만들었다.
- [코드 1-2]에서는 x 좌표값과 y 좌표값이 모두 0인지, 즉, 초기 위치로 되돌아왔는지를 검사하는 함수인 if_comeback(x, y)가 정의되어 있다.
#### [코드 1-1]
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
```
#### [코드 1-2]
```python
def if_comeback(x, y):
    return x == 0 and y == 0
```
#### [코드 1-3]
```python
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
#### [결과 1]
```plaintext
23
```
#### --> 정답은 10이지만, 23이 나왔다.
<br/>

### 구현 과정 - 2
- 좌표의 변화를 확인하기 위해, [코드 1-3]을 [코드 2]로 수정하였다.
- [코드 2]는 [코드 1-3]에 현재 위치의 좌표를 출력하는 코드를 추가한 코드이다.
#### [코드 2]
answer = 0
for i in range(n):
    inputCommand = input().split()
    direction, distance = inputCommand[0], int(inputCommand[1])
    dir_num = dirDict[direction]
    for j in range(distance):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        print(x, y)
        answer += 1
        if if_comeback(x, y):
            break
# answer = if_comeback(x, y) and answer or -1
print(answer)
