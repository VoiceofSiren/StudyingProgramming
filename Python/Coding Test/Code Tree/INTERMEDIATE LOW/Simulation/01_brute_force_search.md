# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/best-place-of-33?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >

#### [코드 1-1]
```python
n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
```
#### [코드 1-2]
```python
def count_coins(i, j, square):
    count_value = 0
    for i in range(i, i+3):
        for j in range(j, j+3):
            if square[i][j] == 1:
                count_value += 1
    return count_value
```
#### [코드 1-3]
```python
max_value = 0
for i in range(n-2):
    for j in range(n-2):
        coin_value = count_coins(i, j, square)
        if coin_value > max_value:
            max_value = coin_value
print(max_value)
```
#### [결과 1]
```python
Traceback (most recent call last):
  File "/tmp/Main.py", line 16, in <module>
    coin_value = count_coins(i, j, square)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/Main.py", line 8, in count_coins
    if square[i][j] == 1:
       ^^^^^^^^^^^^
IndexError: list index out of range
```
#### --> 인덱스 처리에 유의하여 코드를 다시 작성하겠다.
<br/>

### < 구현 과정 - 2 >
- [코드 1-2]를 [코드 2-1]로, [코드 1-3]을 [코드 2-2]로 수정하였다.
#### [코드 2-1]
```python
def count_coins(i, j, square):
    count_value = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            count_value += square[x][y]
    return count_value
```
#### [코드 2-2]
```python
max_value = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        max_value = max(max_value, count_coins(i, j, square))
print(max_value)
```
#### [결과 2]
```plaintext
4
```
#### --> 결과가 정상적으로 출력되었음을 확인할 수 있다.
