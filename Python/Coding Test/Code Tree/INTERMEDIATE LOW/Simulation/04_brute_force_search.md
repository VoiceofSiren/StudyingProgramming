# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/conveyor-belt-triangle?&utm_source=clipboard&utm_medium=text
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
n, t = tuple(map(int, input().split()))
c_belt = [list(map(int, input().split())) for i in range(3)]
```
#### [코드 1-2]
```python
def rotate(c_belt):
    temp_list = []
    for i in range(3):
        temp_list.append(c_belt[i][n-1])
    print(temp_list)
    for i in range(3):
        for j in range(n-1, 0, -1):
            c_belt[i][j] = c_belt[i][j-1]
            print(f'{c_belt[i][j]} <= {c_belt[i][j-1]}')
        c_belt[i][0] = temp_list[(i + 2) % 3]
```
#### [코드 1-3]
```python
for _ in range(t):
    rotate(c_belt)

for row in c_belt:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 1]
```plaintext
[4, 3, 1]
2 <= 2
1 <= 1
9 <= 9
5 <= 5
5 <= 5
6 <= 6
1 1 2 
4 5 9 
3 6 5 
```
#### --> 문제에서 요구하는 결과를 도출하기 위해 중간에 좌표를 출력해보는 코드를 추가하였다.
#### 정답 부분만 보니 로직이 정확한 것 같다. (한 번에 맞출 줄은 몰랐다...)
<br/>

### < 구현 과정 - 2 >
- [코드 2]는 [코드 1-2]에서 불필요한 print()를 제거한 코드이다.
#### [코드 2]
```python
def rotate(c_belt):
    temp_list = []
    for i in range(3):
        temp_list.append(c_belt[i][n-1])
    for i in range(3):
        for j in range(n-1, 0, -1):
            c_belt[i][j] = c_belt[i][j-1]
        c_belt[i][0] = temp_list[(i + 2) % 3]
```
#### [결과 2]
```plaintext
1 1 2 
4 5 9 
3 6 5
```
#### --> 정답이 잘 도출되었음을 확인할 수 있다.
