# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/cross-shape-bomb?&utm_source=clipboard&utm_medium=text
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
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
print(f'selected_num: square[{r}][{c}] = {square[r][c]}')
```
#### [코드 1-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 1-3]
```python
def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count):
        for j in range(c - loop_count, c + loop_count):
            if not in_range(i, j):
                continue
            else:
                square[i][j] = 0
```
#### [코드 1-4]
```python
def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value
```
#### [코드 1-5]
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
#### [코드 1-6]
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
#### [코드 1-7]
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
#### [코드 1-8]
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
#### --> 0이 십자가 모양으로 출력되어야 하는데 사각형 모양으로 떴고 범위도 뭔가 잘못된 것 같다.
<br/>

### < 구현 과정 - 2 >
- [코드 1-3]에 있던 explode() 함수에 i와 j의 범위를 마지막 한 칸씩 늘려주고고 Debugging을 위한 print() 코드를 추가하였다.
- 폭발하는 범위가 십자가이기 위해서는 이중 for문을 돌리면 안 되고 x 축 기준으로 한 번, y 축 기준으로 for문을 한 번씩 돌려야 한다는 사실을 깨달았다.
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
#### --> 폭발하는 함수는 정상적으로 동작함을 확인했다.
<br/>

### < 구현 과정 - 3 >
- 각 열에서 마지막 0의 index를 구해오는 함수와 폭발 후 떨어지는 함수를 일부 수정하였다.
#### [코드 3-1]
```python
def get_index_of_last_zero(column):
    index = len(column) - 1
    for c in column:
        if c == 0:
            break
        else:
            index -= 1
    return index - 1
```
#### [코드 3-2]
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
#### --> ei (end index) 값이 뭔가 이상하다...
<br/>

### < 구현 과정 - 4 >
- Debugging을 위한 print()를 없애보았다.
- 애석하게도 다른 테스트케이스에서 오답이 발생하였다.
#### [코드 4-1]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
print(f'selected_num: square[{r}][{c}] = {square[r][c]}')
```
#### [코드 4-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 4-3]
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
#### [코드 4-4]
```python
def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value
```
#### [코드 4-5]
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
#### [코드 4-6]
```python
def get_index_of_last_zero(column):
    index = n - 1
    for index in range(n-1, -1, -1):
        if column[index] == 0:
            break
    return index
```
#### [코드 4-7]
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
```
#### [코드 4-8]
```python
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
- 각 열에서 마지막 0의 index를 구하는 함수의 로직이 잘못되었음을 깨닫고 수정하였다.
- 각 열에서 0의 개수에 따라 요소를 shift시키는 로직을 수정하였다.
- Debugging을 위한 print() 코드를 주석으로 처리하였다.
#### [코드 5-1]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
# print(f'selected_num: square[{r}][{c}] = {square[r][c]}')
```
#### [코드 5-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 5-3]
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
    # print('--- explode ---')
    # for row in square:
    #     for element in row:
    #         print(element, end=' ')
    #     print()
    # print('---------------')           
```
#### [코드 5-4]
```python
def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value
```
#### [코드 5-5]
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
#### [코드 5-6]
```python
def get_index_of_last_zero(column):
    index = n - 1
    for index in range(n-1, -1, -1):
        if column[index] == 0:
            break
    return index
```
#### [코드 5-7]
```python
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
```
#### [코드 5-8]
```python
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
#### --> 다른 테스트 케이스에 대하여도 정답이 정상적으로 출력된 것을 확인할 수 있다.
