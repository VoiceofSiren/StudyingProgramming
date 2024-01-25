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
    count_value = 1
    for i in range(n):
        if square[i][j] == square[i][j+1]:
            count_value += 1
            print(f'h: x={i}, y={j}, cv={count_value}')
            if count_value == m:
                return 1
        else:
            count_value = 1
    return 0

def vertical_search(i, square):
    count_value = 1
    for j in range(n):
        if square[i][j] == square[i+1][j]:
            count_value += 1
            print(f'v: x={i}, y={j}, cv={count_value}')
            if count_value == m:
                return 1
        else:
            count_value = 1
    return 0

answer = 0
for i in range(loop_count): # i = 0, 1
    answer += vertical_search(i, square)

for j in range(loop_count): # j = 0, 1
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
#### --> 문제에서 주어진 조건을 만족하는 좌표를 console에 출력해 보았더니, 내가 작성한 로직의 본질적인 문제점을 파악했다.
#### m개의 연속되는 수열만 체크하다 보니, m개보다 더 많이 연속되는 수열도 한 개로 계산해야 하는데 여러 번 카운트된다.
<br/>

### < 구현 과정 - 4 >
- 별도의 순열 list를 만들고 수직 탐색과 수평 탐색 시 그때마다 순열 list를 새로 초기화해주는 방식으로 코드를 다시 짰다.
#### [코드 4-1]
```python
n, m = list(map(int, input().split()))
square = [list(map(int, input().split())) for _ in range(n)]
sequence = [0 for _ in range(n)]

def is_happy():
    consecutive_count, max_count = 1, 1
    for i in range(1, n):
        if sequence[i - 1] == sequence[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        max_count = max(max_count, consecutive_count)
    return max_count >= m


happy_count = 0
for i in range(n):
    sequence = square[i][:]
    if is_happy():
        happy_count += 1


for j in range(n):
    for i in range(n):
        sequence[i] = square[i][j]
    if is_happy():
            happy_count += 1

print(happy_count)
```
#### [결과 4]
```plaintext
