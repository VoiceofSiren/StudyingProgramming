# Arrow Function
<br/>

### 이 글의 목적
    - Arrow Function (화살표 함수)에 대하여 알아보고자 한다.
    - 이번 글에서는 화살표 함수의 문법뿐만 아니라 더 자세한 내용을 다루고자 한다.
<br/>

### 1. Arguments & Parameters
- 일반 함수와 화살표 함수는 arguments와 parameters에서 차이점을 가진다.
#### 1) 일반함수 - Arguments
- function 키워드를 사용하여 정의한 일반 함수에는 별도로 정의해주지 않아도 arguments라는 변수를 암묵적으로 전달받는다.
#### [코드 1-1]
```javascript
function main() {
    console.log(arguments)
}
```
#### [코드 1-2]
```javascript
main()
```
#### [결과 1]
```plaintext
Arguments [callee: ƒ, Symbol(Symbol.iterator): ƒ]
```
