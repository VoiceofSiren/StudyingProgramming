# Persistence Management
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
- 엔티티 객체를 메모리에 보관하고 관리하는 저장소이다.
- EntityManager 객체를 통해 영속성 컨텍스트에 접근한다.
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
<br/>

#### 캐시 (Cache)
- 영속성 컨텍스트와 관련하여 중요한 개념 중 하나는 캐시이다.
- DBMS에 접근하는 것은 많은 시스템 자원을 소모하기 때문에, DBMS로의 접근을 최소화하기 위해 고안된 방법이 캐시를 활용하는 것이다.
- 캐시는 1차 캐시와 2차 캐시로 구분된다.
#### 1) 1차 캐시
```plaintext
- 영속성 컨텍스트 내에서 엔티티 객체를 보관하는 캐시이다.
- 1차 캐시는 트랜잭션의 시작 시점부터 종료 시점까지만 유효하다.
- 한 트랜잭션 내에 DB에서 조회한 객체를 담고 있으며, 동일한 객체를 DB에서 조회하려는 경우 1차 캐시에 있는 객체가 우선적으로 조회된다.
- 이와 관련된 대표적인 메서드는 EntityManager의 persist(), flush(), clear() 등이 있다.
```
#### 2) 2차 캐시
```plaintext
- 애플리케이션 범위의 캐시로서, 애플리케이션이 종료될 때까지 유지된다.
- 동시성을 극대화하기 위해 캐시한 객체를 직접 반환하지 않고 복사본을 만들어서 반환한다.
```
<br/>

### 3. Life Cycle of Entity (엔티티의 생명 주기)
- 엔티티는 다음과 같은 네 가지 상태 중 하나를 가진다.
#### 1) 비영속 (New / Transient)
```plaintext
- 새로 만들어진 객체의 상태.
- 영속 상태로 진입하기 이전의 상태.
- 예: [코드 1]의 일부분인 [코드 2-1]에서의 객체 obj의 상태이다.
```
#### [코드 2-1]
```java
Object obj = new Object();
```
#### 2) 영속 (Managed)
```plaintext
- 영속성 컨텍스트에 의해 관리되는 상태.
- 예: [코드 1]의 일부분인 [코드 2-2]에서의 객체 obj의 상태이다.
```
#### [코드 2-2]
```java
em.persist(obj);
```
#### 3) 준영속 (Detached)
```plaintext
- Managed 상태에서 영속성 컨텍스트로부터 분리된 상태.
- 예: [코드 2-3]에서는 영속성 컨텍스트를 완전히 비우는 clear() 메서드의 예시를 보여준다.
```
#### [코드 2-3]
```java
em.clear();
```
#### 4) 삭제 (Removed)
```plaintext
- 영속성 컨텍스트에서 삭제된 상태.
- 예: [코드 2-4]에서는 객체를 삭제하는 remove() 메서드의 예시를 보여준다.
```
#### [코드 2-4]
```java
em.remove(obj);
```
