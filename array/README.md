# 데이터 구조 - Array of C and List of Python

C에는 Array가 있고 이를 응용하여 여러 종류의 List들을 만들 수 있다.

또한 Python에서 이와 비슷하게 List가 있다

먼저 C의 Array와 그를 응용한 사례들을 소개하겠다.

## C

### Array
---

```c
int arr[4];
```
int는 자료형을, arr은 array 이름을, 그리고 [4]는 해당 array의 크기를 의미한다.

**Array는 선언할 때에 자료형과 크기가 결정되고 변경할 수 없다.**

### Linked List
---
Array를 응용하여 linked list를 만들어준다면 자유로운 자료형과 크기를 가질 수 있다.

Linked List는 크기가 2인 배열을 사용하여 앞에는 값을 뒤에는 다음 배열의 주소를 할당하여 만들 수 있다.
다음 배열의 자료형은 앞의 배열의 자료형과 다를 수 있으며, 다음 배열의 주소를 할당하여 만들기에 배열을 자유롭게 수정할 수 있다. 

하지만 사용할 값 하나에 크기가 2인 배열을 사용하기에 같은 수의 값을 저장할 때에 Array보다 두배 많은 메모리 공간을 차지한다. 또한 마지막 자리에 다음 배열의 주소만 할당되기에 다음 값을 찾기에는 유리하지만 그 이전에 있는 값을 찾기엔 불리하다.

### Doubly Linked List
---
Doubly Linked List는 크기가 3인 배열을 사용하여 Linked List의 단점인 한 값의 이전 값을 찾기 용이하게 만든 리스트이다. 0번 자리에 앞 배열의 주소, 1번 자리에 값, 그리고 2번 자리에 다음 배열의 주소를 할당하여 앞뒤로 모두 이동하기에 용이한 배열이다. 하지만 Array보다 세배 많은 메모리 공간을 차지한다.

## Python

Python에서는 C와 달리 리스트를 여러가지 만들 필요가 없다.

파이썬에서는 ```list```라는 자료형이 있다.

이의 기본적인 구조는 C의 Array와 같지만 작동하는 방식이 조금 다르다.

```python
arr = []
l = list()
```
파이썬의 list는 위와 같이 선언할 수 있고, 이는 크기가 정해지지 않은 C의 Array와 비슷하다.

C의 Array는 고정된 크기를 가지고 배열에 정해진 자료형의 값을 저장하지만 Python List는 크기를 계속해서 수정할 수 있으며 list에 값을 그대로 저장하는 방식이 아니라 독립적인 object를 만들고 그 object의 주소를 저장한다.
독립적인 object를 만들기에 object의 자료형을 자유롭게 선택할 수 있다.

<image src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbiBuQ8%2Fbtslw75X9rR%2FDk9cfnN0Qc5Nqk9xqwI5Sk%2Fimg.png" alt="python list">
