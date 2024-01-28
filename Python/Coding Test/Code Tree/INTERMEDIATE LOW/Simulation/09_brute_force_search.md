# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/sequential-movement-of-numbers?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 각 칸에서 최댓값을 구한 후 각 칸에서 다시 dx dy Technique를 활용해 해당 칸에서 반복문을 돌리다가 최댓값일 때 멈추는 방식으로 구현하고자 한다.
#### [코드 1-1]
```python
