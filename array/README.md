# 데이터 구조 - Array and List in C and Python

C에는 Array와 Linked List가 있다.

또한 Python에는 List가 있다

먼저 C의 사례들을 소개하겠다.

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
Linked List는 Array와 달리 자료형과 크기를 변경할 수 있다.

Linked List는 Value와 Next로 구성된 구조체를 사용하여 만든다.

다음 배열의 자료형은 앞의 배열의 자료형과 다를 수 있으며, 다음 배열의 주소를 할당하여 만들기에 배열을 자유롭게 수정할 수 있다. 

하지만 같은 크기의 데이터에 array보다 많은 메모리를 사용하기에 같은 수의 값을 저장할 때에 Array보다 두배 많은 메모리 공간을 차지한다. Next에는 Value의 주소만 할당되기에 다음 값을 찾기에는 유리하지만 그 이전에 있는 값을 찾기엔 불리하다.

### Doubly Linked List
---
Doubly Linked List는 Previous 포인터, Value, 그리고 Next 포인터로 구성된 구조체를 사용하여 만든다. Linked List의 단점인 한 값의 이전 값을 찾기 용이하게 만든 리스트이다. 순서대로 이전 value의 주소, value, 그리고 다음 value의 주소가 할당된다. 하지만 linked list보다 메모리 공간을 차지하는 단점이있다.

## Python

Python에서는 C의 array, linked list와 비슷하지만 다른 list 자료형이 있다.

이의 기본적인 구조는 C의 Array와 같지만 작동하는 방식이 조금 다르다.

```python
arr = []
l = list()
```
파이썬의 list는 위와 같이 선언할 수 있다.

C의 Array는 고정된 크기를 가지고 배열에 정해진 자료형의 값을 저장하지만 Python List는 크기를 계속해서 수정할 수 있으며 list에 값을 그대로 저장하는 방식이 아니라 독립적인 object를 만들고 그 object의 주소를 저장한다.
독립적인 object를 만들기에 object의 자료형을 자유롭게 선택할 수 있다.

<image src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbiBuQ8%2Fbtslw75X9rR%2FDk9cfnN0Qc5Nqk9xqwI5Sk%2Fimg.png" alt="python list">
