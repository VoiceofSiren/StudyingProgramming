# Persistence
<br/>

### 이 글의 목적
- JPA에서 객체를 DBMS에 저장할 때 어떤 과정을 거치는지 알아보고자 한다.
<br/>

### 1. Transaction (트랜잭션)
- JPA를 통해 객체를 DBMS에 CRUD할 때 기본적으로 트랜잭션 단위로 수행된다.
- 각각의 독립된 트랜잭션은 EntityTransaction 객체가 begin()할 때 시작되고
  EntityTransaction 객체가 commit()할 때 종료되며,
  트랜잭션이 실행되는 도중 Exception이 발생할 경우 rollback()으로 실행을 취소한다.
- 결과적으로 commit()을 해야만 Hibernate에서 생성된 SQL문이 DBMS에 반영된다.
- [코드 1]는 트랜잭션 내에서 Object 객체를 DB에 저장하는 코드의 예시이다.
#### [코드 1]
```java
public class JpaMain {

    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();

        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            Object obj = new Object();
            /*
            codes to develop
            */
            em.persist(obj);    // SQL문 생성
            tx.commit();        // 생성된 SQL문을 DBMS에 실제로 적용하는 단계
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }

        emf.close();
    }
}
```
<br/>

### 2. Persistence Context (영속성 컨텍스트) 
- 엔티티 객체를 메모리에 보관하고 관리하는 환경이다.
- 영속성 컨텍스트가 제공하는 기능들은 다음과 같다.
#### [기능 1] - 엔티티 객체 캐싱
```plaintext
- 영속성 컨텍스트는 엔티티 객체를 메모리에 캐싱하여 데이터베이스 접근 횟수를 줄이고 성능을 향상시킨다.
```
#### [기능 2] - 엔티티 객체 상태 추적
```plaintext
- 영속성 컨텍스트는 엔티티 객체의 상태를 추적하고 변경 사항을 감지한다.
```
#### [기능 3] - 변경 사항 동기화
```plaintext
- 영속성 컨텍스트는 트랜잭션이 끝날 때 엔티티 객체의 변경 사항을 데이터베이스에 동기화한다.
```
- 영속성 컨텍스트와 관련하여 중요한 개념 중 하나는 캐시 (Cache)이다.
- 캐시는 1차 캐시와 2차 캐시로 구분된다.
#### 1) 1차 캐시
```plaintext
- 영속성 컨텍스트 내에서 엔티티 객체를 보관하는 캐시이다.
- 이와 관련된 대표적인 메서드는 EntityManager의 persist(), flush(), clear() 등이 있다.
```
#### 2) 2차 캐시
```plaintext
2차 캐시: 여러 영속성 컨텍스트에서 공유되는 캐시입니다.
5. 영속성 컨텍스트 동작 방식:

엔티티 객체가 영속성 컨텍스트에 저장되면 영속 상태로 변경됩니다.
영속 상태의 엔티티 객체는 메모리에 캐싱되고 변경 사항은 추적됩니다.
트랜잭션이 끝날 때 영속성 컨텍스트는 변경 사항을 데이터베이스에 동기화합니다.
엔티티 객체가 영속성 컨텍스트에서 제거되면 준영속 상태로 변경됩니다.
```
<br/>

### 3. Life Cycle of Entity (엔티티의 생명 주기)
- 
