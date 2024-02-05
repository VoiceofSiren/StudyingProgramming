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

