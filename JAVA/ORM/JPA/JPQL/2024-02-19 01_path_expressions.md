# Path Expressions
<br/>

### 이 글의 목적
    - JPQL의 Path Expressions (경로 표현식)에 대하여 알아보고자 한다.
<br/>

### 1. Dot Notation
- .을 사용하여 엔터티의 필드나 연관 관계를 탐색하는 방식.
#### [JPQL]
```plaintext
SELECT **m.username**    
  FROM Member m
  JOIN m.team t
  JOIN m.orders o
WHERE t.name = '팀A'
```
