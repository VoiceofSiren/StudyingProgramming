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
#### [코드 1-2]는 myFilter()를 호출하는 코드이다.
#### [결과 1]은 [코드 1-1]과 [코드 1-2]를 실행했을 때 console에 출력되는 결과이다.
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
    newWords = myFilter(words, (element) => {
        return element.length > 6;
    })
    console.log(newWords);
```
#### [결과 1]
  ['exuberant', 'destruction', 'present']

### myFilter() 구현 과정
    1. 파라미터로 문자열을 요소로 갖는 배열과 





  
