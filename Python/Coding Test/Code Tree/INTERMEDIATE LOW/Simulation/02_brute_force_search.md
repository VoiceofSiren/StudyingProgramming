# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/number-of-happy-sequence?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >

#### [코드 1-1]
```python
n, m = list(map(int, input().split()))
square = [list(map(int, input().split())) for _ in range(n)]
loop_count = n - m + 1

def horizontal_search(i, j, square):
    count_value = 0
    for y in range(j, j + loop_count):
        if square[i][j] == square[i][j+1]:
            count_value += 1
        else:
            count_value = 0
        if count_value == m:
            return 1
    return 0

def vertical_search(i, j, square):
    count_value = 0
    for x in range(i, i + loop_count):
        if square[i][j] == square[i+1][j]:
            count_value += 1
        else:
            count_value = 0
        if count_value == m:
            return 1
    return 0

answer = 0
for i in range(n):
    for j in range(n):
        answer += horizontal_search(i, j, square)
        answer += vertical_search(i, j, square)

print(answer)
```
#### [결과 1]
```plaintext
Traceback (most recent call last):
  File "/tmp/Main.py", line 30, in <module>
    answer += horizontal_search(i, j, square)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/Main.py", line 8, in horizontal_search
    if square[i][j] == square[i][j+1]:
                       ^^^^^^^^^^^^^^
IndexError: list index out of range
```
<br/>

### < 구현 과정 - 2 >

#### [코드 2-1]
```python
n, m = list(map(int, input().split()))
square = [list(map(int, input().split())) for _ in range(n)]
loop_count = n - m + 1

def in_range(x, y):
    return 0 <= x <= n-1 and 0 <= y <= n-1

def horizontal_search(j, square):
    count_value = 0
    for i in range(n):
        for y in range(j, j + m):
            if square[i][y] == square[i][y+1]:
                count_value += 1
            else:
                count_value = 0
            if count_value == m - 1:
                return 1
    return 0

def vertical_search(i, square):
    count_value = 0
    for j in range(n):
        for x in range(i, i + m):
            if square[x][j] == square[x+1][j]:
                count_value += 1
            else:
                count_value = 0
            if count_value == m - 1:
                return 1
    return 0

answer = 0
for i in range(loop_count):
    answer += vertical_search(i, square)

for j in range(loop_count):
    answer += horizontal_search(j, square)

print(answer)
```
#### [결과 2]
```plaintext
4
```
<br/>

### < 구현 과정 - 3 >

#### [코드 3-1]
```python
n, m = list(map(int, input().split()))
square = [list(map(int, input().split())) for _ in range(n)]
loop_count = n - m + 1

def in_range(x, y):
    return 0 <= x <= n-1 and 0 <= y <= n-1

def horizontal_search(j, square):
    count_value = 0
    for i in range(n):
        if square[i][j] == square[i][j+1]:
            count_value += 1
            print(f'h: x={i}, y={j}, cv={count_value}')
            if count_value == m - 1:
                return 1
        else:
            count_value = 0
    return 0

def vertical_search(i, square):
    count_value = 0
    for j in range(n):
        if square[i][j] == square[i+1][j]:
            count_value += 1
            print(f'v: x={i}, y={j}, cv={count_value}')
            if count_value == m - 1:
                return 1
        else:
            count_value = 0
    return 0

answer = 0
for i in range(loop_count):
    answer += vertical_search(i, square)

for j in range(loop_count):
    answer += horizontal_search(j, square)

print(answer)
```
#### [결과 3]
```plaintext
v: x=0, y=0, cv=1
v: x=1, y=0, cv=1
h: x=0, y=1, cv=1
3
```
