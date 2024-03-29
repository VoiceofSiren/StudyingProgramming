# Relationship
<br/>

### 이 글의 목적
```plaintext
- JPA의 Relationship Mapping (연관관계 매핑)에 대해 알아보고자 한다.
- 이번 글에서는 연관관계의 주인 대해 알아볼 것이다.
```
<br/>

### 1. 연관관계의 주인 매핑
- DBMS에서는 외래키 제약이 걸린 두 테이블 간 양방향으로 데이터를 조회할 수 있다.
- JAVA는 객체로 한 방향씩 참조하기 때문에 양방향 연관관계의 경우 두 객체 중 하나를 연관관계의 주인으로 지정해줘야 한다.
- 결과적으로, 외래키를 가지고 있는 테이블을 연관관계의 주인으로 지정하면 된다.
- 연관관계의 주인만이 외래키를 관리할 수 있으며, 주인이 아닌쪽은 읽기만 가능하다.
- [그림 1]에 따르면, MEMBER 테이블이 외래키를 가지고 있으므로 연관관계의 주인은 MEMBER이다.
#### 1) 주인인 객체 (Owner side)
#### [그림 1]
![IMAGE](../../../images/tableRelationship0007.png)
#### [코드 1-1]
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
- Team 타입 필드인 team에 @JoinColumn(name = "team_id")을 사용한다.
- DBMS에서 외래키를 통해 데이터를 조회할 경우 기본적으로 JOIN 연산자를 사용하는데, 해당 JOIN 연산 시에 사용되는 외래키의 이름을 지정해줘야만 한다.
<br/>

#### 2) 주인이 아닌 객체 (Non-owner side)
#### [코드 1-2]
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
- List<Member> 타입 필드인 members에 @OneToMany(mappedBy = "team")를 사용한다.
- 주인이 아닌 쪽은 반드시 mappedBy를 통해 주인 쪽의 필드명을 지정해줘야만 한다.
