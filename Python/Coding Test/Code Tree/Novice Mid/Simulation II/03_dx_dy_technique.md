# dx dy technique
###### Question: https://www.codetree.ai/missions/5/problems/comfortable-state-on-the-grid?&utm_source=clipboard&utm_medium=text
<br/>

### 이 글의 목적
    - dx dy Technique를 활용하여 문제를 풀어볼 것이다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- [코드 1-2]에서는 x와 y의 좌표 값이 square 인덱스 범위 밖으로 나갔는지 검사하는 함수가 정의되어 있다.
- [코드 1-3]에는 문제에서 주어진 편안한 상태를 검사하는 함수가 정의되어 있다. 
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
#### --> 2차원 배열의 인덱스와 관련하여 잘못 설정한 것 같다. 에러를 수정해보자.
<br/>

### < 구현 과정 - 2 >
- [코드 2-3]에서 in_range(x, y) 함수를 if_comfortable(x, y) 함수 내부에 넣었다.
- [코드 2-3]에서 nx, ny를 설정해놓고 조건문에 적용하지 않아 [코드 3-3]에 수정할 내용을 적용하였다.
- [코드 2-3]을 수정함에 따라 [코드 2-4]의 조건문이 일부 수정되었다.
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
#### [결과 2]
```plaintext
0
0
0
1
0
0
1
0
```
#### --> 정답이 잘 도출되었음을 확인할 수 있다.
