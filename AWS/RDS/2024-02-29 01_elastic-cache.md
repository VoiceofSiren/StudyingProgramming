# Elastic Cache
<br/>

### 이 글의 목적
    - RDS의 성능 개선을 위해 사용하는 Elastic Cache에 대해 알아보고자 한다.
<br/>

### 1. Elastic Cache
```plaintext
- 클라우드 내에서 In-memory Cache를 만든다.
- DB가 아니라 Cache에서 데이터를 읽기 때문에 데이터를 빨리 읽어올 수 있다.
- Read-heavy 애플리케이션에서 상당한 Latency 감소 효과를 가져온다.
- 애플리케이션 개발 초기 단계에서의 사용은 적합하지 않다.
```
<br/>

 ### 2. Type of Elastic Cache
 #### 1) Memcached
```plaintext
- Object Cache System으로 잘 알려져 있다.
- Elastic Cache는 default로 Memcached의 프로토콜을 따른다.
- EC2 Auto Scaling처럼 데이터 사용량에 따라 크기가 유동적으로 변할 수 있다.
- 무료 오픈소스이다.
```
 #### 2) Redis
 ```plaintext
- Key-Value, Set, List와 같은 형태의 데이터를 In-memory에 저장할 수 있다.
- Multi-AZ를 지원한다. 즉, 재해 복구 기능이 있다.
- 무료 오픈소스이다.
```
