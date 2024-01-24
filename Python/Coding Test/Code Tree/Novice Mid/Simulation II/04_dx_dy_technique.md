# dx dy Technique
###### Question: https://www.codetree.ai/missions/5/problems/shoot-a-laser-in-the-mirror-2?&utm_source=clipboard&utm_medium=text
###### Difficulty: Hard
<br/>

### 이 글의 목적
    - dx dy Technique를 활용하여 문제를 풀어볼 것이다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 그동안에는 Zero-padding 기법을 사용하지 않았지만, 좌표평면 상에서 거울이 있는 범위의 밖에서 접근해야 하기 때문에 Zero-padding 기법을 사용해야 할 것 같은 느낌이 든다.
#### [코드 1]
```python
n = int(input())

mirrors = [[0 for j in range(n + 2)] for i in range(n + 2)]
for i in range(1, n + 1):
    row = input()
    for j in range(1, n + 1):
        mirrors[i][j] = row[j-1]

for row in mirrors:
    for element in row:
        print(element, end=' ')
    print()
```
#### [결과 1]
```plaintext
0 0 0 0 0 
0 / \ \ 0 
0 \ \ \ 0 
0 / \ / 0 
0 0 0 0 0 
```
#### --> 일단 Zero-padding이 잘 되었음을 확인할 수 있다.
<br/>

### < 구현 과정 - 2 >

#### [그림 1-1]
![IMAGE](../images/mirror01.png)
#### [그림 1-2]
![IMAGE](../images/mirror02.png)
#### [그림 1-3]
![IMAGE](../images/mirror03.png)
#### [코드 2]
```python

```
#### [결과 2]
```plaintext

```
