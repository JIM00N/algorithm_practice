# Graph

### 정의
노드(N, node)와 그 노드를 연결하는 간선(E, edge)을 하나로 모아 놓아 연결되어 있는 객체 간의 관계를 표현할 수 있는 자료구조.

![graph](https://img.notionusercontent.com/s3/prod-files-secure%2F971703c5-12f6-4793-8670-fe9d2d59dbab%2F9c0cd02e-3424-40bb-bcb9-2f72383e0eb1%2FUntitled.png/size/w=930?exp=1727157096&sig=kQtZCvKOeqHk9pGpOckypzvKOinvrQl9hnvjsZlR4tE)

### 구성요소
1. 노드 혹은 정점 (node or vertex) : <br>
개별적인 요소이다. 사람, 도시 등 다양한 대상이 될 수 있다. 예를 들어, 소셜 네트워크에서 정점은 사람을 나타낼 수 있다.

2. 간선 (Edge / Link / Branch) : <br>
두 정점을 연결하는 선으로, 정점 간의 관계를 나타낸다.

### 종류
![그래프종류](https://file.notion.so/f/f/971703c5-12f6-4793-8670-fe9d2d59dbab/5f794761-c3e3-43c3-b7ca-a983ab06c5f1/Untitled.png?table=block&id=c09a3298-d32d-49d8-8fb1-71754b9de94a&spaceId=971703c5-12f6-4793-8670-fe9d2d59dbab&expirationTimestamp=1727164800000&signature=VuszXDCwvmvXUNrdtJAROTgGKXAO4aUSJYwdha5Ggas&downloadName=Untitled.png)

### 관련 용어
- 인접 정점(adjacent vertex): 간선에 의 해 직접 연결된 정점
- 정점의 차수(degree): 무방향 그래프에서 하나의 정점에 인접한 정점의 수
- 무방향 그래프에 존재하는 정점의 모든 차수의 합 = 그래프의 간선 수의 2배
- 진입 차수(in-degree): 방향 그래프에서 외부에서 오는 간선의 수 (내차수 라고도 부름)
- 진출 차수(out-degree): 방향 그래프에서 외부로 향하는 간선의 수 (외차수 라고도 부름)
- 방향 그래프에 있는 정점의 진입 차수 또는 진출 차수의 합 = 방향 그래프의 간선의 수(내차수 + 외차수)
- 경로 길이(path length): 경로를 구성하는 데 사용된 간선의 수
- 단순 경로(simple path): 경로 중에서 반복되는 정점이 없는 경우
- 사이클(cycle): 단순 경로의 시작 정점과 종료 정점이 동일한 경우

### Graph Tree 차이점

|      |<center>그래프|<center>트리 |
|------|------|------|
|<center>정의 |노드와 그 노드를 연결하는 간선을 하나로 모아놓은 자료 구조 | 그래프의 한 종류, DAC의 한 종류 |
|<center>방향성 |방향/무방향 그래프 모두 존재 | 방향그래프 |
|<center>사이클 | 사이클 가능, 자체 간선도 가능, 순환 그래프, 비순환 그래프 모두 존재 | 사이클 불가능, 자체 간선도 불가능, 비순환 그래프만 존재 |
|<center>루트 노드|루트 노드의 개념이 없음|한 개의 루트 노드만이 존재, 모든 자식 노드는 한개의 부모 노드만을 가짐|
|<center>부모자식|부모-자식의 개념 없음|부모-자식 관계 top-bottom 또는 bottom-top으로 이루어짐|
모델|네트워크 모델|계층 모델|
순회|DFS, BFS|DFS, BFS안의 Pre-, In-, Post-order|
|<center>간선의 수|그래프에 따라 간선의 수가 다름, 간선이 없을 수도 있음|노드가 N인 트리는 항상 N-1의 간선을 가짐|
|<center>경로| - |임의의 두 노드 간의 경로는 유일|
|<center>예시 및 종류|지도, 지하철 노선도의 최단 경로, 전기 회로의 소자들, 도로, 선수 과목|이진 트리, 이진 탐색 트리, 균형 트리, 이진 힙 등|