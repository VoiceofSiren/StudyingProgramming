# Callback Function
<br/>

### 이 글의 목적
    - callback/2024-01-16 02_callbackFunction.md에서 callback function의 구체적인 예시를 통해 학습하였다.
    - 이번 글을 통해 callback function을 직접 구현해 보면서 실력을 향상시키고자 한다.
<br/>

### Array.prototype.filter() API
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter에서 확인 가능.
    - filter() API를 나만의 함수로 직접 구현해 보고자 한다.

#### [코드 1-1]은 filter() API를 나만의 함수로 구현한 myFilter()를 나타내며,
#### [코드 1-2]는 fx라는 콜백 함수를 정의하고 myFilter()를 호출하는 코드이다.
#### [결과 1]은 [코드 1-1]과 [코드 1-2]를 실행했을 때 console에 출력되는 결과이다.

### myFilter() 구현 과정
    1. 파라미터로 문자열을 요소로 갖는 배열과 콜백 함수를 넣는다.
    2. 반환 값으로 필요한 비어있는 배열 result를 선언한다.
    3. 배열의 첫 번째 원소부터 마지막 원소까지 순회하면서, 콜백 함수를 조건으로 하여 true일 때 
       배열 result에 해당 원소를 넣는다.
    4. 배열 result를 반환한다.

### fx 구현 과정
    1. element의 길이가 6을 초과하면 true를 반환한다.

#### [코드 1-1]
```plaintext
    const words = ['spray', 'elite', 'exuberant', 'destruction', 'present'];
    function myFilter(arr, callbackFunc) {
        var result = [];
        for (let i=0; i < arr.length; i++) {
            var current = arr[i];
            if (callbackFunc(current)) {
                result.push(current);
            }
        }
        return result;
    }
```
#### [코드 1-2]
```plaintext
    fx = (element) => {
        return element.length > 6;
    };

    newWords = myFilter(words, fx);
    console.log(newWords);
```
#### [결과 1]
  ['exuberant', 'destruction', 'present']
    
#### --> [결과 1]을 통해 Array.prototype.filter() API를 사용했을 때와 동일한 결과가 나왔음을 확인할 수 있다.
<br/>

### 콜백 함수 코드 간략화
#### [코드 1-2]에서 콜백 함수 fx는 다음의 두 가지 특징을 가진다.
        1. 파라미터가 1개이다.
        2. {} 블록 안에 return문 한 줄만 있다.
#### 위의 특징을 만족하는 콜백 함수의 경우, 두 가지 과정을 거쳐 간략화할 수 있다.
        1. 파라미터의 괄호를 없앤다.
        2. {} 중괄호와 return과 ; (세미 콜론)을 없앤고 한 줄로 정리한다.
#### [코드 1-3]은 [코드 1-2]를 간략화한 코드이다.
#### [코드 1-3]
```plaintext
    newWords = myFilter(words, element => element.length > 6);
    console.log(newWords);
```
#### [코드 1-3]의 형식은 개발자들이 굉장히 많이 사용하는 코드 형식이라고 하니 원리를 잘 이해하고 익숙해지도록 하자.



  
