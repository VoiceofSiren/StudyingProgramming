# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/sequential-movement-of-numbers?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 각 칸에서 최댓값을 구한 후 각 칸에서 다시 dx dy Technique를 활용해 해당 칸에서 반복문을 돌리다가 최댓값일 때 멈추는 방식으로 구현하고자 한다.
#### [코드 1-1]
```python
n, m = tuple(map(int, input().split()))
square = [
    list(map(int, input().split()))
    for _ in range(n)
]

#    EE  SE SS SW WW NW  NN  NE
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
```
#### [코드 1-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 1-3]
```python
def find_position(num):
    position = (0, 0)
    for i in range(n):
        for j in range(n):
            if num == square[i][j]:
                position = (i, j)
                break
    return position
```
#### [코드 1-4]
```python
def get_max_value(x, y):
    max_value = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value
```
#### [코드 1-5]
```python
def get_position_to_change(x, y, square):
    max_value = get_max_value(x, y)
    position_to_change = (0, 0)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        if max_value == square[nx][ny]:
            position_to_change = (nx, ny)
            break
    return position_to_change
```
#### [코드 1-6]
```python
for num in range(1, m + 1):
    x, y = find_position(num)
    max_value = get_max_value(x, y)
    p, q = get_position_to_change(x, y, square)
    square[x][y], square[p][q] = square[p][q], square[x][y]

for row in square:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 1]
```plaintext
15 1 13 11 
4 8 3 5 
2 12 16 7 
14 6 9 10
```
#### --> 오답이 출력되었다. 
<br/>

### < 구현 과정 - 2 >
- 이번에도 문제를 잘못 이해하였다. 각 턴마다 하나의 숫자를 기준으로 위치를 바꾸는 것인 줄 알았지만, 각 턴마다 모든 칸을 조회해야 하는 것이었다.
#### [코드 2-1]
```python
n, m = tuple(map(int, input().split()))
square = [
    list(map(int, input().split()))
    for _ in range(n)
]

#    EE  SE SS SW WW NW  NN  NE
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
```
#### [코드 2-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 2-3]
```python
def get_max_value(x, y, square):
    max_value = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value
```
#### [코드 2-4]
```python
def get_position_to_change(x, y, square):
    max_value = get_max_value(x, y, square)
    position_to_change = (0, 0)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        if max_value == square[nx][ny]:
            position_to_change = (nx, ny)
            break
    return position_to_change
```
#### [코드 2-5]
```python
def change_all(square):
    for num in range(1, n * n + 1):
        for i in range(n):
            for j in range(n):
                if square[i][j] == num:
                    # x, y: current_position
                    x, y = i, j
                    # p, q: position_to_change
                    p, q = get_position_to_change(x, y, square)
                    square[p][q], square[x][y] = square[x][y], square[p][q]
```
#### [코드 2-6]
```python
for _ in range(m):
    change_all(square)

for row in square:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 2]
```plaintext
4 1 13 11 
8 12 3 5 
2 15 6 7 
14 9 16 10
```
#### --> 이번에도 오답이 출력되었다. Debugging을 위한 print()코드를 추가하여 원인을 분석해보고자 한다.
<br/>

### < 구현 과정 - 3 >
- Debugging을 위한 print()코드를 추가하였다.
#### [코드 3-1]
```python
n, m = tuple(map(int, input().split()))
square = [
    list(map(int, input().split()))
    for _ in range(n)
]

#    EE  SE SS SW WW NW  NN  NE
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
```
#### [코드 3-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 3-3]
```python
def get_max_value(x, y, square):
    max_value = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value
```
#### [코드 3-4]
```python
def get_position_to_change(x, y, square):
    max_value = get_max_value(x, y, square)
    position_to_change = (0, 0)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        if max_value == square[nx][ny]:
            position_to_change = (nx, ny)
            break
    return position_to_change
```
#### [코드 3-5]
```python
def change_all(square):
    for num in range(1, n * n + 1):
        for i in range(n):
            for j in range(n):
                if square[i][j] == num:
                    # x, y: current_position
                    x, y = i, j
                    # p, q: position_to_change
                    p, q = get_position_to_change(x, y, square)
                    print(f'num = {num} / (x, y) = ({x}, {y}) / (p, q) = ({p}, {q})')
                    square[p][q], square[x][y] = square[x][y], square[p][q]
```
#### [코드 3-6]
```python
for _ in range(m):
    change_all(square)

for row in square:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 3]
```plaintext
num = 1 / (x, y) = (0, 2) / (p, q) = (0, 1)
num = 2 / (x, y) = (2, 0) / (p, q) = (3, 0)
num = 2 / (x, y) = (3, 0) / (p, q) = (2, 0)
num = 3 / (x, y) = (1, 2) / (p, q) = (2, 2)
num = 3 / (x, y) = (2, 2) / (p, q) = (1, 2)
num = 4 / (x, y) = (1, 0) / (p, q) = (0, 0)
num = 5 / (x, y) = (1, 3) / (p, q) = (2, 2)
num = 5 / (x, y) = (2, 2) / (p, q) = (1, 3)
num = 6 / (x, y) = (3, 1) / (p, q) = (2, 2)
num = 7 / (x, y) = (2, 3) / (p, q) = (3, 3)
num = 7 / (x, y) = (3, 3) / (p, q) = (2, 3)
num = 8 / (x, y) = (1, 1) / (p, q) = (1, 0)
num = 9 / (x, y) = (3, 2) / (p, q) = (3, 1)
num = 10 / (x, y) = (3, 3) / (p, q) = (3, 2)
num = 11 / (x, y) = (0, 3) / (p, q) = (0, 2)
num = 12 / (x, y) = (2, 1) / (p, q) = (1, 1)
num = 13 / (x, y) = (0, 3) / (p, q) = (0, 2)
num = 14 / (x, y) = (3, 0) / (p, q) = (2, 1)
num = 15 / (x, y) = (3, 0) / (p, q) = (2, 1)
num = 16 / (x, y) = (3, 3) / (p, q) = (3, 2)
4 1 13 11 
8 12 3 5 
2 15 6 7 
14 9 16 10 

```
#### --> num 값은 턴마다 1씩 증가해야 하는데 그렇지 않은 경우가 발생했음을 확인할 수 있다.
<br/>

### < 구현 과정 - 4 >
- 왜 같은 num 값에 대하여 두 번 실행되는 구간이 있을까를 고민하던 끝에, 반복문을 돌다가 이미 바뀐 위치에 해당 num 값이 또 있으면 로직이 또 돌아가서 해당 숫자들이 다시 원위치된다는 사실을 알아냈다.
- [코드 3-5]에 있는 change_all() 함수를 수정하였다.
#### [코드 4]
```python
def change_all(square):
    for num in range(1, n * n + 1):
        if_changed = False
        for i in range(n):
            for j in range(n):
                if if_changed == True:
                    continue
                if square[i][j] == num:
                    # x, y: current_position
                    x, y = i, j
                    # p, q: position_to_change
                    p, q = get_position_to_change(x, y, square)
                    square[p][q], square[x][y] = square[x][y], square[p][q]
                    if_changed = True
```
#### [결과 4]
```plaintext
4 1 13 11 
8 12 5 7 
6 15 3 9 
2 14 16 10 
```
#### --> 정답이 정상적으로 출력되었음을 확인할 수 있다.
