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
#### [코드 1-1]
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

### < 구현 과정 - 1 >
- k 위치는 (k - 1) 인덱스를 가리키므로 k 값을 입력 받자마자 1만큼 감소시켜 계산에 혼동이 없도록 하였다.
#### [코드 1-1]
```python
