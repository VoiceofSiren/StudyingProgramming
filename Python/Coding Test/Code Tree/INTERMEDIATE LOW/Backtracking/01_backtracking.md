# Backtracking
###### Question: https://www.codetree.ai/missions/2/problems/n-permutation?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - Backtracking 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >

#### [코드 1-1]
```python
n = int(input())
arr = []
visited = [ 0 for _ in range(n)]

def print_arr():
    for element in arr:
        print(element + 1, end=' ')
    print()

def make_permutations(current_num):
    if current_num == n:
        print_arr()
        return
    
    for i in range(n):
        arr.append(i)
        visited[i] = 1
        make_permutations(current_num + 1)
        visited[arr.pop()] = 0

make_permutations(0)
```
#### [결과 1]
```plaintext
1 1 1 
1 1 2 
1 1 3 
1 2 1 
1 2 2 
1 2 3 
1 3 1 
1 3 2 
1 3 3 
2 1 1 
2 1 2 
2 1 3 
2 2 1 
2 2 2 
2 2 3 
2 3 1 
2 3 2 
2 3 3 
3 1 1 
3 1 2 
3 1 3 
3 2 1 
3 2 2 
3 2 3 
3 3 1 
3 3 2 
3 3 3 

```
#### --> 각 순열에는 중복되는 숫자가 나오면 안 되지만 [결과 1]에서는 중복되는 숫자가 출력되었음을 확인할 수 있다.
