# dx dy technique
###### Question: https://www.codetree.ai/missions/5/problems/come-back-2?&utm_source=clipboard&utm_medium=text
<br/>

### 이 글의 목적
    - dx dy Technique를 활용하여 문제를 풀어볼 것이다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### 구현 과정 - 1
- 방향에 따른 dx 배열과 dy 배열의 index 값을 맞춰주기 위해 [코드 1-1]에서 command_dict를 만들었다.
- [코드 1-2]에서는 x 좌표값과 y 좌표값이 모두 0인지, 즉, 초기 위치로 되돌아왔는지를 검사하는 함수인 if_comeback(x, y)가 정의되어 있다.
#### [코드 1-1]
```python
x, y = 0, 0

#     E  S  W   N
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

command_dict = {
    'L': 3, # -1
    'R': 1,
    'F': 0
}

dir_num = 3
```
#### [코드 1-2]
```python
def if_comeback(x, y):
    return x == 0 and y == 0
```
#### [코드 1-3]
```python
command = input()

time = 0
for i in range(len(command)):
    dir_num = (dir_num + command_dict[command[i]]) % 4
    time += 1
    if command[i] == 'F':
        x = x + dx[command_dict[command[i]]]
        y = y + dy[command_dict[command[i]]]
    if x == 0 and y == 0:
        break
print(time)
```
#### [결과 1]
```plaintext
17
```
#### --> 정답은 13이지만 17이라는 오답이 출력되었다.
<br/>

### 구현 과정 - 2
