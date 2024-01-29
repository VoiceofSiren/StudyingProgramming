# Backtracking
###### Question: https://www.codetree.ai/missions/2/problems/max-of-xor?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - Backtracking 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 윷놀이 게임 중 각 턴을 돌리면서 나올 수 있는 최대 점수를 출력해야 한다.
- 각 말들이 이동하면서 각 말들에 이동할 칸의 값을 더하여 윷놀이 판의 길이보다 크거나 같은지를 비교한다.
#### [코드 1-1]
```python
