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
- 경로 탐색의 끝으로서, 더 이상 경로 탐색이 불가하다.
    - 예: m.username
<br/>

### 3. Association Field (연관 필드)
- 연관 관계를 위한 필드.
- 단일 값 연관 필드와 컬렉션 값 연관 필드가 있다.
#### 1) Single-valued Association Path (단일 값 연관 경로)
- 연관 관계의 대상이 Entity인 필드.
- 묵시적 INNER JOIN이 발생하며, 경로 탐색 가능하다.
    - 예: m.team
```java
@ManyToOne
@OneToOne
```
#### [코드 1]
```java
String query = "select m.team from Member m";
```
#### [결과 1]
```plaintext
Hibernate: 
    /* select
        m.team 
    from
        Member m */ select
            t1_0.team_id,
            t1_0.name 
        from
            member m1_0 
        join
            team t1_0 
                on t1_0.team_id=m1_0.team_id
```
#### --> 별도의 JPQL에 JOIN 문을 입력하지 않아도 묵시적으로 JOIN 문이 실행되는 것을 확인할 수 있다.
#### 2) Collection-valued Association Path (컬렉션 값 연관 경)
- 연관 관계의 대상이 Collection인 필드.
- 묵시적 INNER JOIN이 발생하며, 더 이상 경로 탐색이 불가하다.
- 단, FROM 절에서 명시적 JOIN을 통해 별칭을 얻으면 별칭을 통해 탐색할 수 있다.
    - 예: m.orders
```java
@OneToMany
@ManyToMany
```
#### [코드 2-1] - 가능
```java
String query = "select t.members from Team t";
```
#### [코드 2-2] - 불가능
```java
String query = "select t.members.username from Team t";
```
#### [코드 2-3] - 가능
```java
String query = "select m.username from Team t join t.members m";
```
