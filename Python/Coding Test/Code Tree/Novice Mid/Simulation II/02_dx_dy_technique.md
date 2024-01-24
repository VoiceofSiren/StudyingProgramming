# dx dy technique
<br/>

#### [코드 1]
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
