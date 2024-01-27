# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/falling-horizontal-block?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- k 위치는 (k - 1) 인덱스를 가리키므로 k 값을 입력 받자마자 1만큼 감소시켜 계산에 혼동이 없도록 하였다.
#### [코드 1]
```python
n, m, k = tuple(map(int, input().split()))
k = k - 1

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

block = []
for i in range(n):
    if k <= i < k + m:
        block.append(1)
    else:
        block.append(0)

print('block')
for b in block:
    print(b, end= ' ')
print()

print('matrix')
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 1]
```plaintext
block
1 1 1 0 
matrix
0 0 0 0 
0 0 0 1 
1 0 0 1 
1 1 1 1
```
#### --> 문제에서 주어진 입출력이 정상적으로 이루어졌음을 확인했다.
<br/>

### < 구현 과정 - 2 >
- 문제에서 주어진 조건식에 대해 곰곰히 따져보니, 같은 열에 있는 블록의 값과 블록이 이동할 칸의 값이 둘 다 1만 아니면 다음 줄로 넘어갈 수 있는지 여부를 판가름할 수 있겠다고 문득 떠올랐다.
#### [코드 2-1]
```python
n, m, k = tuple(map(int, input().split()))
k = k - 1

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

block = []
for i in range(n):
    if k <= i < k + m:
        block.append(1)
    else:
        block.append(0)
```
#### [코드 2-2]
```python
def ok_to_move(i):
    flag = 0
    for j in range(n):
        if block[j] == 1 and matrix[i + 1][j] == 1:
            continue
        else:
            flag += 1
    return flag == n
```
#### [코드 2-3]
```python
i = 0
while True:
    if ok_to_move(i):
        i += 1
    else:
        for j in range(n):
            if matrix[i][j] == 0 and block[j] == 1:
                matrix[i][j] = block[j]
        break

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 2-1]
```python
0 0 0 0 
1 1 1 1 
1 0 0 1 
1 1 1 1 
```
#### --> 정답이 출력되었지만, 애석하게도 다른 테스트 케이스에서 런타임 에러가 발생하였다...
#### [결과 2-2]
```plaintext
Traceback (most recent call last):
  File "/tmp/Main.py", line 30, in <module>
    if ok_to_move(i):
       ^^^^^^^^^^^^^
  File "/tmp/Main.py", line 21, in ok_to_move
    if block[j] == 1 and matrix[i + 1][j] == 1:
                         ^^^^^^^^^^^^^
IndexError: list index out of range
```
<br/>

### < 구현 과정 - 3 >
- 다른 테스트 케이스에 대하여도 맞도록 반복문에서의 초기 인덱스 값을 수정하였으며, 행의 값이 n을 넘어가는 경우에 대한 조건문도 추가하였다.
#### [코드 3-1]
```python
n, m, k = tuple(map(int, input().split()))
k = k - 1

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

block = []
for i in range(n):
    if k <= i < k + m:
        block.append(1)
    else:
        block.append(0)
```
#### [코드 3-2]
```python
def ok_to_move(i):
    flag = 0
    for j in range(n):
        if block[j] == 1 and matrix[i + 1][j] == 1:
            continue
        else:
            flag += 1
    # print('flage =', flag)
    return flag == n
```
#### [코드 3-3]
```python
i = -1
while True:
    if ok_to_move(i):
        i += 1
        if i + 1 >= n:
            for j in range(n):
                if block[j] == 1:
                    matrix[i][j] = 1
            break
    else:
        for j in range(n):
            if block[j] == 1:
                matrix[i][j] = 1
        break

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 3]
```plaintext
1
```
#### --> 정답이 출력되었음을 확인할 수 있다.
