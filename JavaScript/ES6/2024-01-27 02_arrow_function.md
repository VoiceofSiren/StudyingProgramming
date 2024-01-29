# Arrow Function
<br/>

### 이 글의 목적
    - Arrow Function (화살표 함수)에 대하여 알아보고자 한다.
    - 이번 글에서는 화살표 함수의 문법뿐만 아니라 더 자세한 내용을 다루고자 한다.
<br/>

### 1. Arguments & Parameters
- 일반 함수와 화살표 함수는 arguments와 parameters에서 차이점을 가진다.
#### 1) 일반함수 - Arguments
#### [코드 1]
```javascript
function main() {
    console.log(arguments)
}

main()
```
#### [결과 1]
```plaintext
Arguments [callee: ƒ, Symbol(Symbol.iterator): ƒ]
```
