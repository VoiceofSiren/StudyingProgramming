# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/move-to-larger-adjacent-cell?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- r행 c열은 (r-1, c-1) 인덱스에 있는 요소를 가리키므로 r, c 값을 입력 받자마자 1만큼 감소시켜 계산에 혼동이 없도록 하였다.
#### [코드 1-1]
```python
n, r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
square = [list(map(int, input().split())) for _ in range(n)]

#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(r, c):
    dir_num, max_value = 0, 0
    for dir_num in range(4):
        nx = r + dx[dir_num]
        ny = c + dy[dir_num]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    
    for dir_num in range(4):
        nx = r + dx[dir_num]
        ny = c + dy[dir_num]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] == max_value:
            break
    r = r + dx[dir_num]
    c = c + dy[dir_num]
    print(square[r][c], end=' ')

for _ in range(5):
    move(r, c)
```
#### [결과 1]
```plaintext
10 10 10 10 10
```
<br/>

### < 구현 과정 - 2 >
- r행 c열은 (r-1, c-1) 인덱스에 있는 요소를 가리키므로 r, c 값을 입력 받자마자 1만큼 감소시켜 계산에 혼동이 없도록 하였다.
#### [코드 2-1]
```python
n, r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
square = [list(map(int, input().split())) for _ in range(n)]
print(f'r = {r}, c = {c}, square[{r}][{c}] = {square[r][c]}')
print('===============================')
#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max_value():
    max_value = 0
    for dir_num in range(4):
        nx = r + dx[dir_num]
        ny = c + dy[dir_num]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value

def move(r, c):
    dir_num = 0
    max_value = get_max_value()
    print('max_value =', max_value)
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] == max_value:
            dir_num = i
            break
    print('dir_num =', dir_num)
    r = r + dx[dir_num]
    c = c + dy[dir_num]
    print(f'r = {r}, c = {c}, square[{r}][{c}] = {square[r][c]}')
    print('-------------------------------')

for _ in range(5):
    move(r, c)
```
#### [결과 2]
```plaintext
r = 1, c = 1, square[1][1] = 5
===============================
max_value = 10
dir_num = 3
r = 1, c = 2, square[1][2] = 10
max_value = 10
dir_num = 3
r = 1, c = 2, square[1][2] = 10
max_value = 10
dir_num = 3
r = 1, c = 2, square[1][2] = 10
max_value = 10
dir_num = 3
r = 1, c = 2, square[1][2] = 10
max_value = 10
dir_num = 3
r = 1, c = 2, square[1][2] = 10
```
<br/>

### < 구현 과정 - 3 >
- r과 c 값이 변하지 않았음을 확인할 수 있다.
- global 키워드를 사용하기로 하였다.
#### [코드 3-1]
```python
n, r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
square = [list(map(int, input().split())) for _ in range(n)]
print(f'r = {r}, c = {c}, square[{r}][{c}] = {square[r][c]}')
print('===============================')
#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max_value():
    max_value = 0
    for dir_num in range(4):
        nx = r + dx[dir_num]
        ny = c + dy[dir_num]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value

def move():
    global r, c
    dir_num = 0
    max_value = get_max_value()
    print('max_value =', max_value)
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] == max_value:
            dir_num = i
            break
    print('dir_num =', dir_num)
    r = r + dx[dir_num]
    c = c + dy[dir_num]
    print(f'r = {r}, c = {c}, square[{r}][{c}] = {square[r][c]}')
    print('-------------------------------')

for _ in range(5):
    move()
```
#### [결과 3]
```plaintext
r = 1, c = 1, square[1][1] = 5
===============================
max_value = 10
dir_num = 3
r = 1, c = 2, square[1][2] = 10
-------------------------------
max_value = 15
dir_num = 3
r = 1, c = 3, square[1][3] = 15
-------------------------------
max_value = 10
dir_num = 2
r = 1, c = 2, square[1][2] = 10
-------------------------------
max_value = 15
dir_num = 3
r = 1, c = 3, square[1][3] = 15
-------------------------------
max_value = 10
dir_num = 2
r = 1, c = 2, square[1][2] = 10
-------------------------------
```
<br/>

### < 구현 과정 - 4 >
- 애석하게도 필자가 문제를 잘못 이해하고 있었다.
- 선택된 칸을 기준으로 상하좌우 칸 중 최댓값과 비교하는 것이 아니라, 선택된 칸을 기준으로 상하좌우로 비교하다가 더 큰 값을 가지는 칸을 만나면 그 방향으로 바로 이동하는 문제였다.
#### [코드 4-1]
```python
n, r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
square = [list(map(int, input().split())) for _ in range(n)]
print(f'r = {r}, c = {c}, square[{r}][{c}] = {square[r][c]}')
print('===============================')
#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def compare():
    dir_num = -1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] > square[r][c]:
            dir_num = i
            break
    return dir_num

def move():
    global r, c
    dir_num = compare()

    if dir_num == -1:
        return False
    
    print('dir_num =', dir_num)
    r = r + dx[dir_num]
    c = c + dy[dir_num]
    print(f'r = {r}, c = {c}, square[{r}][{c}] = {square[r][c]}')
    print('-------------------------------')
    return True

while True:
    m = move()
    if m == False:
        break
```
#### [결과 4]
```plaintext
r = 1, c = 1, square[1][1] = 5
===============================
dir_num = 1
r = 2, c = 1, square[2][1] = 8
-------------------------------
dir_num = 3
r = 2, c = 2, square[2][2] = 11
-------------------------------
```
#### --> Debugging을 위한 print()만 없애면 정답일 것 같다.
<br/>

### < 구현 과정 - 5 >
- Debugging을 위한 print()만 없앴다.
#### [코드 5]
```python
n, r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1
square = [list(map(int, input().split())) for _ in range(n)]

print(square[r][c], end=' ')

#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def compare():
    dir_num = -1
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] > square[r][c]:
            dir_num = i
            break
    return dir_num

def move():
    global r, c
    dir_num = compare()

    if dir_num == -1:
        return False
    
    r = r + dx[dir_num]
    c = c + dy[dir_num]
    print(square[r][c], end=' ')
    return True

while True:
    m = move()
    if m == False:
        break
```
#### [결과 5]
```plaintext
5 8 11 
```
#### --> 정답이 출력되었음을 확인할 수 있다.
