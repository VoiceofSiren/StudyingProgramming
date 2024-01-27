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
