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
```python
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
```
#### [결과 2]
```plaintext
-1 0
-2 0
-3 0
-3 1
-3 2
-2 2
-1 2
0 2
0 1
0 0
1 0
2 0
3 0
4 0
5 0
5 1
5 2
5 3
5 4
5 5
5 6
5 7
5 8
23
```
#### --> [결과 2]의 '0 0'에서 break문이 작동해야 하는데, 멈추지 않고 반복문이 계속 이어지는 것을 확인할 수 있다.
<br/>

### 구현 과정 - 3
- [코드 2]를 [코드 3]으로 수정하였다.
- 원위치로 돌아오지 않았을 때의 정답값을 -1로 설정해놓고, 반복문을 수행하면서 원위치로 돌아왔을 경우에만 경과한 시간의 값을 정답에 대입하여 결과를 출력하는 방식으로 수정하였다.
#### [코드 3]
```python
answer = -1
time = 0
for i in range(n):
    inputCommand = input().split()
    direction, distance = inputCommand[0], int(inputCommand[1])
    dir_num = dirDict[direction]
    for j in range(distance):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        time += 1
        if if_comeback(x, y):
            answer = time
            break
print(answer)
```
#### [결과 3]
```
10
```
#### --> 정답이 잘 도출된 것을 확인할 수 있다.
