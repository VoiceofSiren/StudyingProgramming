# Relationship
<br/>

### 이 글의 목적
```plaintext
- JPA의 Relationship Mapping (연관관계 매핑)에 대해 알아보고자 한다.
- 이번 글에서는 연관관계의 주인 대해 알아볼 것이다.
```
<br/>

### 1. 연관관계의 주인
- DBMS에서는 외래키 제약이 걸린 두 테이블 간 양방향으로 데이터를 조회할 수 있다.
- JAVA는 객체로 한 방향씩 참조하기 때문에 양방향 연관관계의 경우 두 객체 중 하나를 연관관계의 주인으로 지정해줘야 한다.

#### [코드 1-1]
```java
@Entity
@Getter
@Setter
public class Team {

    @Id
    @GeneratedValue
    @Column(name = "team_id")
    private Long id;

    @OneToMany(mappedBy = "team")
    private List<Member> members = new ArrayList<>();

    private String teamName;
}
```
#### [코드 1-2]
```java
@Entity
@Getter
@Setter
public class Member {

    @Id
    @GeneratedValue
    @Column(name = "member_id")
    private Long id;

    private String memberName;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "team_id")
    private Team team;
}
```
