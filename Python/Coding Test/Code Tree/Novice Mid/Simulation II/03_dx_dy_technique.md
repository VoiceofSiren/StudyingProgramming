# dx dy technique
###### Question: [https://www.codetree.ai/missions/5/problems/come-back-2?&utm_source=clipboard&utm_medium=text](https://www.codetree.ai/missions/5/problems/comfortable-state-on-the-grid?&utm_source=clipboard&utm_medium=text)
<br/>

### 이 글의 목적
    - dx dy Technique를 활용하여 문제를 풀어볼 것이다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### 구현 과정 - 1
- 방향에 따른 dx 배열과 dy 배열의 index 값을 맞춰주기 위해 [코드 1-1]에서 command_dict를 만들었다.
- [코드 1-2]에서는 x 좌표값과 y 좌표값이 모두 0인지, 즉, 초기 위치로 되돌아왔는지를 검사하는 함수인 if_comeback(x, y)가 정의되어 있다.
#### [코드 1-1]
```python
n, m = list(map(int, input().split()))

square = [[0 for _ in range(n)] for _ in range(n)]

#     E  S  W   N
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
```
#### [코드 1-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 1-3]
```python
def if_comfortable(x, y):
    count_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if square[nx][ny] == 1:
            count_value += 1
    return count_value >= 3
```
#### [코드 1-4]
```python
for i in range(m):
    r, c = list(map(int, input().split()))
    x, y = r-1, c-1
    square[x][y] = 1
    if in_range(x, y) and if_comfortable(x,y):
        print(1)
    else:
        print(0) 
```
#### [결과 1]
```plaintext
Traceback (most recent call last):
  File "/tmp/Main.py", line 28, in <module>
    if in_range(x, y) and if_comfortable(x,y):
                          ^^^^^^^^^^^^^^^^^^^
  File "/tmp/Main.py", line 19, in if_comfortable
    if square[nx][ny] == 1:
       ^^^^^^^^^^
IndexError: list index out of range
```
####
<br/>

#### [코드 2-1]
```python
n, m = list(map(int, input().split()))

square = [[0 for _ in range(n)] for _ in range(n)]

#     E  S  W   N
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
```
#### [코드 2-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 2-3]
```python
def if_comfortable(x, y):
    count_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny):
            if square[nx][ny] == 1:
                count_value += 1
    return count_value >= 3
```
#### [코드 2-4]
```python
for _ in range(m):
    r, c = list(map(int, input().split()))
    x, y = r-1, c-1
    square[x][y] = 1
    if if_comfortable(x,y):
        print(1)
    else:
        print(0) 
```
