# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/cross-shape-bomb?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 2차원 배열의 각 행의 마지막 원소를 임시 배열에 할당한 후 각 행에서 오른쪽으로 한 칸씩 shift 시킨 후,
- k행의 임시 변수의 값을 (k+1)행의 첫 번째 요소에 할당하는 로직을 구현하고자 한다.
#### [코드 1-1]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
print(f'selected_num: square[{r}][{c}] = {square[r][c]}')
```
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
```python
def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count):
        for j in range(c - loop_count, c + loop_count):
            if not in_range(i, j):
                continue
            else:
                square[i][j] = 0
```
```python
def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value
```
```python
def get_index_of_first_zero(column):
    index = 0
    for c in column:
        if c == 0:
            return index
        else:
            index += 1
    return index
```
```python
def get_index_of_last_zero(column):
    index = len(column) - 1
    for c in column:
        if c == 0:
            break
        else:
            index -= 1
    return index
```
```python
def fall_down(r, c, square):
    for i in range(n):
        column = []
        for j in range(n):
            column.append(square[j][i])
        print('fall_down1:', column)

        zeros = count_zeros(column)
        si = get_index_of_first_zero(column)
        ei = get_index_of_last_zero(column)
        for j in range(ei, si, -1):
            column[j] = column[j - 1]
        for j in range(0, zeros):
            column[j] = 0
        print('fall_down2:', column)
        for j in range(n):
            square[j][i] = column[j]
```
```python
explode(r, c, square)
fall_down(r, c, square)

for i in range(n):
    for j in range(n):
        print(square[i][j], end=' ')
    print()
```
#### [결과 1]
```plaintext
selected_num: square[1][2] = 2
fall_down1: [1, 3, 3, 4]
fall_down2: [1, 3, 3, 4]
fall_down1: [0, 0, 1, 5]
fall_down2: [0, 0, 0, 1]
fall_down1: [0, 0, 6, 4]
fall_down2: [0, 0, 0, 6]
fall_down1: [3, 3, 2, 4]
fall_down2: [3, 3, 2, 4]
1 0 0 3 
3 0 0 3 
3 0 0 2
4 1 6 4 
```
<br/>


### < 구현 과정 - 2 >
- 2차원 배열의 각 행의 마지막 원소를 임시 배열에 할당한 후 각 행에서 오른쪽으로 한 칸씩 shift 시킨 후,
- k행의 임시 변수의 값을 (k+1)행의 첫 번째 요소에 할당하는 로직을 구현하고자 한다.
#### [코드 2-1]
```python
def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count + 1):
        if not in_range(i, 0):
            continue
        else:
            square[i][c] = 0
    for j in range(c - loop_count, c + loop_count + 1):
        if not in_range(0, j):
            continue
        else:
            square[r][j] = 0
    print('--- explode ---')
    for row in square:
        for element in row:
            print(element, end=' ')
        print()
    print('---------------')
```
#### [결과 2]
```plaintext
selected_num: square[1][2] = 2
--- explode ---
1 2 0 3 
3 0 0 0 
3 1 0 2 
4 5 4 4 
---------------
fall_down1: [1, 3, 3, 4]
fall_down2: [1, 3, 3, 4]
fall_down1: [2, 0, 1, 5]
fall_down2: [0, 0, 0, 5]
fall_down1: [0, 0, 0, 4]
fall_down2: [0, 0, 0, 0]
fall_down1: [3, 0, 2, 4]
fall_down2: [0, 0, 0, 4]
1 0 0 0 
3 0 0 0 
3 0 0 0 
4 5 0 4 

```
<br/>


### < 구현 과정 - 3 >
- 2차원 배열의 각 행의 마지막 원소를 임시 배열에 할당한 후 각 행에서 오른쪽으로 한 칸씩 shift 시킨 후,
- k행의 임시 변수의 값을 (k+1)행의 첫 번째 요소에 할당하는 로직을 구현하고자 한다.
#### [코드 3-1]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
print(f'selected_num: square[{r}][{c}] = {square[r][c]}')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count + 1):
        if not in_range(i, 0):
            continue
        else:
            square[i][c] = 0
    for j in range(c - loop_count, c + loop_count + 1):
        if not in_range(0, j):
            continue
        else:
            square[r][j] = 0
    print('--- explode ---')
    for row in square:
        for element in row:
            print(element, end=' ')
        print()
    print('---------------')
            

def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value

def get_index_of_first_zero(column):
    index = 0
    for c in column:
        if c == 0:
            return index
        else:
            index += 1
    return index

def get_index_of_last_zero(column):
    index = len(column) - 1
    for c in column:
        if c == 0:
            break
        else:
            index -= 1
    return index - 1

def fall_down(r, c, square):
    for i in range(n):
        column = []
        for j in range(n):
            column.append(square[j][i])
        print('fall_down1:', column)

        zeros = count_zeros(column)
        si = get_index_of_first_zero(column)
        ei = get_index_of_last_zero(column)
        print(f'zeros = {zeros}, si = {si}, ei = {ei}')
        if zeros > 0:
            if zeros == 1:
                for j in range(si, 0, -1):
                    column[j] = column[j - zeros]
                column[0] = 0
            else:
                for j in range(ei - 1, si, -1):
                    column[j] = column[j - zeros]
                for j in range(zeros):
                    column[j] = 0
        
        print('fall_down2:', column)
        for j in range(n):
            square[j][i] = column[j]

explode(r, c, square)
fall_down(r, c, square)

for i in range(n):
    for j in range(n):
        print(square[i][j], end=' ')
    print()
```
#### [결과 3]
```plaintext
selected_num: square[1][2] = 2
--- explode ---
1 2 0 3 
3 0 0 0 
3 1 0 2 
4 5 4 4 
---------------
fall_down1: [1, 3, 3, 4]
zeros = 0, si = 4, ei = -2
fall_down2: [1, 3, 3, 4]
fall_down1: [2, 0, 1, 5]
zeros = 1, si = 1, ei = 1
fall_down2: [0, 2, 1, 5]
fall_down1: [0, 0, 0, 4]
zeros = 3, si = 0, ei = 2
fall_down2: [0, 0, 0, 4]
fall_down1: [3, 0, 2, 4]
zeros = 1, si = 1, ei = 1
fall_down2: [0, 3, 2, 4]
1 0 0 0 
3 2 0 3 
3 1 0 2 
4 5 4 4
```
<br/>

### < 구현 과정 - 4 >
- debugging을 위한 print()를 없애보았다.
- 애석하게도 다른 테스트케이스에서 오답이 발생하였다.

#### [코드 4]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
print(f'selected_num: square[{r}][{c}] = {square[r][c]}')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count + 1):
        if not in_range(i, 0):
            continue
        else:
            square[i][c] = 0
    for j in range(c - loop_count, c + loop_count + 1):
        if not in_range(0, j):
            continue
        else:
            square[r][j] = 0
    print('--- explode ---')
    for row in square:
        for element in row:
            print(element, end=' ')
        print()
    print('---------------')
            

def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value

def get_index_of_first_zero(column):
    index = 0
    for c in column:
        if c == 0:
            return index
        else:
            index += 1
    return index

def get_index_of_last_zero(column):
    index = n - 1
    for index in range(n-1, -1, -1):
        if column[index] == 0:
            break
    return index

def fall_down(r, c, square):
    for i in range(n):
        column = []
        for j in range(n):
            column.append(square[j][i])
        print('fall_down1:', column)

        zeros = count_zeros(column)
        si = get_index_of_first_zero(column)
        ei = get_index_of_last_zero(column)
        print(f'zeros = {zeros}, si = {si}, ei = {ei}')
        if zeros > 0:
            if zeros == 1:
                for j in range(si, 0, -1):
                    column[j] = column[j - zeros]
                column[0] = 0
            else:
                for j in range(ei, si, -1):
                    column[j] = column[j - zeros]
                for j in range(zeros):
                    column[j] = 0
        
        print('fall_down2:', column)
        for j in range(n):
            square[j][i] = column[j]

explode(r, c, square)
fall_down(r, c, square)

for i in range(n):
    for j in range(n):
        print(square[i][j], end=' ')
    print()
```
#### [결과 4]
```plaintext
selected_num: square[3][3] = 2
--- explode ---
1 1 1 1 1 1 
1 2 4 3 1 1 
3 1 2 0 1 1 
3 1 0 0 0 1 
4 5 4 0 1 1 
1 1 1 1 1 1 
---------------
fall_down1: [1, 1, 3, 3, 4, 1]
zeros = 0, si = 6, ei = 0
fall_down2: [1, 1, 3, 3, 4, 1]
fall_down1: [1, 2, 1, 1, 5, 1]
zeros = 0, si = 6, ei = 0
fall_down2: [1, 2, 1, 1, 5, 1]
fall_down1: [1, 4, 2, 0, 4, 1]
zeros = 1, si = 3, ei = 3
fall_down2: [0, 1, 4, 2, 4, 1]
fall_down1: [1, 3, 0, 0, 0, 1]
zeros = 3, si = 2, ei = 4
fall_down2: [0, 0, 0, 1, 3, 1]
fall_down1: [1, 1, 1, 0, 1, 1]
zeros = 1, si = 3, ei = 3
fall_down2: [0, 1, 1, 1, 1, 1]
fall_down1: [1, 1, 1, 1, 1, 1]
zeros = 0, si = 6, ei = 0
fall_down2: [1, 1, 1, 1, 1, 1]
1 1 0 0 0 1 
1 2 1 0 1 1 
3 1 4 0 1 1 
3 1 2 1 1 1 
4 5 4 3 1 1 
1 1 1 1 1 1 
```
<br/>

### < 구현 과정 - 5 >
- debugging을 위한 print()를 없애보았다.
- 애석하게도 다른 테스트케이스에서 오답이 발생하였다.

#### [코드 5]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
# print(f'selected_num: square[{r}][{c}] = {square[r][c]}')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count + 1):
        if not in_range(i, 0):
            continue
        else:
            square[i][c] = 0
    for j in range(c - loop_count, c + loop_count + 1):
        if not in_range(0, j):
            continue
        else:
            square[r][j] = 0
    # print('--- explode ---')
    # for row in square:
    #     for element in row:
    #         print(element, end=' ')
    #     print()
    # print('---------------')
            

def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value

def get_index_of_first_zero(column):
    index = 0
    for c in column:
        if c == 0:
            return index
        else:
            index += 1
    return index

def get_index_of_last_zero(column):
    index = n - 1
    for index in range(n-1, -1, -1):
        if column[index] == 0:
            break
    return index

def fall_down(r, c, square):
    for i in range(n):
        column = []
        for j in range(n):
            column.append(square[j][i])
        # print('fall_down1:', column)

        zeros = count_zeros(column)
        si = get_index_of_first_zero(column)
        ei = get_index_of_last_zero(column)
        # print(f'zeros = {zeros}, si = {si}, ei = {ei}')
        if zeros > 0:
            if zeros == 1:
                for j in range(si, 0, -1):
                    column[j] = column[j - zeros]
                column[0] = 0
            else:
                for j in range(ei, si, -1):
                    column[j] = column[j - zeros]
                for j in range(zeros):
                    column[j] = 0
        
        # print('fall_down2:', column)
        for j in range(n):
            square[j][i] = column[j]

explode(r, c, square)
fall_down(r, c, square)

for i in range(n):
    for j in range(n):
        print(square[i][j], end=' ')
    print()
```
#### [결과 5]
```plaintext
1 1 0 0 0 1 
1 2 1 0 1 1 
3 1 4 0 1 1 
3 1 2 1 1 1 
4 5 4 3 1 1 
1 1 1 1 1 1 
```
