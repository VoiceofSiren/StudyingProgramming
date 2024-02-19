# Path Expressions
<br/>

### 이 글의 목적
    - JPQL의 Path Expressions (경로 표현식)에 대하여 알아보고자 한다.
<br/>

### 1. Dot Notation
- .을 사용하여 엔터티의 필드나 연관 관계를 탐색하는 방식.
- 상태 필드, 단일 값 연관 필드, 컬렉션 값 연관 필드를 나타내는 경로 표현식이 있다.
#### [JPQL]
```plaintext
SELECT m.username        // 상태 필드
    FROM Member m
    JOIN m.team t        // 단일 값 연관 필드
    JOIN m.orders o      // 컬렉션 값 연관 필드
    WHERE t.name = '팀A'
```
<br/>

### 2. State Field (상태 필드)
- 단순히 값을 저장하기 위한 필드.
    - 예: m.username
<br/>

### 3. Association Field (연관 필드)
- 연관 관계를 위한 필드.
- 단일 값 연관 필드와 컬렉션 값 연관 필드가 있다.
#### 1) Single-valued Association Path (단일 값 연관 필드)
- 연관 관계의 대상이 Entity인 필드.
    - 예: m.team
```java
@ManyToOne
@OneToOne
```
#### 2) Collection-valued Association Path (컬렉션 값 연관 필드)
- 연관 관계의 대상이 Collection인 필드.
    - 예: m.orders
```java
@OneToMany
@ManyToMany
```
