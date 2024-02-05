# Persistence
<br/>

### 이 글의 목적
- JPA에서 객체를 DBMS에 저장할 때 어떤 과정을 거치는지 알아보고자 한다.
<br/>

### 1. Transaction (트랜잭션)
- JPA를 통해 객체를 DBMS에 CRUD할 때 기본적으로 트랜잭션 단위로 수행된다.


Persistence의 의미:

데이터베이스에 데이터를 영구적으로 저장하는 기능
객체의 상태를 데이터베이스에 저장하고,
