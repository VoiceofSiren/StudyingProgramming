# Backtracking
###### Question: https://www.codetree.ai/missions/2/problems/beautiful-number?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - Backtracking 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 가능한 모든 순열의 경우를 출력해야 한다.
- 중복 검사를 위한 visited 리스트를 사용한다.
#### [코드 1-1]
```python
n = int(input())
arr = []
answer = 0

def in_range(x):
    return 0 <= x < n

def if_arr_beautiful():
    for num in range(1, 5):
        count_value = 0
        for i in range(n - (num - 1)):
            for j in range(i, i + num):
                if arr[j] == num:
                    count_value += 1
                if count_value == num:
                    return True
    return False
                

def count_beautiful_numbers(answer):
    if if_arr_beautiful():
        answer += 1

def myFunc(num_count):
    if num_count == n:
        count_beautiful_numbers(answer)
        return
    
    for i in range(n):
        arr.append(i)
        myFunc(num_count + 1)
        arr.pop()


myFunc(0)
print(answer)
```
#### [결과 1]
```plaintext
0
```
#### --> 오답이 출력되었다. Debugging을 통해 어떤 부분이 잘못되었는지 확인하고자 한다.
<br/>

### < 구현 과정 - 2 >
- 1, 2, 3, 4 숫자의 인덱스를 각각 받을 수 있는 2차원 배열을 사용해보는 게 어떨까 라는 생각이 들었다.
#### [코드 2-1]
```python
n = int(input())
arr = []
visited = [
    [] for _ in range(4)
]
answer = 0

def in_range(x):
    return 0 <= x < n

def print_arr(arr):
    print('print_arr()')
    print('[ ', end='')
    for element in arr:
        print(element, end=' ')
    print(']')

def print_visited(visited):
    if len(arr) == n:
        print('print_visited()')
        for row in visited:
            print('[ ', end='')
            for element in row:
                print(element, end=' ')
            print(']')

def if_arr_beautiful(visited):
    beautiful = False
    for i in range(4):
        if i == 0:
            if len(visited[i]) >= 1:
                beautiful = True
        elif i == 1:
            if len(visited[i]) >= 2:
                for j in range(len(visited[i]) - 1):
                    if visited[i] == visited[i + 1]:
                        beautiful = True
        elif i == 2:
            if len(visited[i]) >= 3:
                for j in range(len(visited[i]) - 2):
                    if visited[i] == visited[i + 1] and visited[i + 1] == visited[i + 2]:
                        beautiful = True
        else:
            if len(visited[i]) >= 4:
                for j in range(len(visited[i]) - 3):
                    if  visited[i] == visited[i + 1] and visited[i + 1] == visited[i + 2] and  visited[i + 2] == visited[i + 3]:
                        beautiful = True 
    return beautiful
                

def count_beautiful_numbers(answer):
    if if_arr_beautiful(visited):
        answer += 1

def myFunc(num_count):
    if num_count == n:
        count_beautiful_numbers(answer)
        return
    
    for i in range(4):
        arr.append(i + 1)
        visited[i].append(num_count)
        print_visited(visited)
        myFunc(num_count + 1)
        arr.pop()
        visited[i].pop()


myFunc(0)
print(answer)
```
#### [결과 2]
```plaintext
print_visited()
[ 0 1 2 ]
[ ]
[ ]
[ ]
print_visited()
[ 0 1 ]
[ 2 ]
[ ]
[ ]
print_visited()
[ 0 1 ]
[ ]
[ 2 ]
[ ]
print_visited()
[ 0 1 ]
[ ]
[ ]
[ 2 ]
print_visited()
[ 0 2 ]
[ 1 ]
[ ]
[ ]
print_visited()
[ 0 ]
[ 1 2 ]
[ ]
[ ]
print_visited()
[ 0 ]
[ 1 ]
[ 2 ]
[ ]
print_visited()
[ 0 ]
[ 1 ]
[ ]
[ 2 ]
print_visited()
[ 0 2 ]
[ ]
[ 1 ]
[ ]
print_visited()
[ 0 ]
[ 2 ]
[ 1 ]
[ ]
print_visited()
[ 0 ]
[ ]
[ 1 2 ]
[ ]
print_visited()
[ 0 ]
[ ]
[ 1 ]
[ 2 ]
print_visited()
[ 0 2 ]
[ ]
[ ]
[ 1 ]
print_visited()
[ 0 ]
[ 2 ]
[ ]
[ 1 ]
print_visited()
[ 0 ]
[ ]
[ 2 ]
[ 1 ]
print_visited()
[ 0 ]
[ ]
[ ]
[ 1 2 ]
print_visited()
[ 1 2 ]
[ 0 ]
[ ]
[ ]
print_visited()
[ 1 ]
[ 0 2 ]
[ ]
[ ]
print_visited()
[ 1 ]
[ 0 ]
[ 2 ]
[ ]
print_visited()
[ 1 ]
[ 0 ]
[ ]
[ 2 ]
print_visited()
[ 2 ]
[ 0 1 ]
[ ]
[ ]
print_visited()
[ ]
[ 0 1 2 ]
[ ]
[ ]
print_visited()
[ ]
[ 0 1 ]
[ 2 ]
[ ]
print_visited()
[ ]
[ 0 1 ]
[ ]
[ 2 ]
print_visited()
[ 2 ]
[ 0 ]
[ 1 ]
[ ]
print_visited()
[ ]
[ 0 2 ]
[ 1 ]
[ ]
print_visited()
[ ]
[ 0 ]
[ 1 2 ]
[ ...(truncated)
```
#### --> 너무 멀리 간 듯 하다. 처음부터 다시 구현해야겠다.
<br/>

### < 구현 과정 - 3 >
- 이차원 배열을 빼고 일차원 배열을 이용하여 구현하였다.
- is_beautiful() 함수 내부에서 최소 길이와 숫자의 연속을 확인하는 로직을 추가하였다.
#### [코드 3-1]
```python
n = int(input())
answer = 0
arr = []


def is_beautiful():
    i = 0
    while i < n:
        if i + arr[i] - 1 >= n:
            return False

        for j in range(i, i + arr[i]):
            if arr[j] != arr[i]:
                return False
        i += arr[i]
        
    return True


def count_beautiful_numbers(cnt):
    global answer
    
    if cnt == n:
        if is_beautiful():
            answer += 1
        return
	
    for i in range(1, 5):
        arr.append(i)
        count_beautiful_numbers(cnt + 1)
        arr.pop()


count_beautiful_numbers(0)
print(answer)
```
#### [결과 3]
```plaintext
4
```
#### --> 난이도가 낮은 문제인데 꽤 오래 걸렸다. 알고리즘 문제를 위한 Backtracking 로직을 잘 숙지해야겠다.
