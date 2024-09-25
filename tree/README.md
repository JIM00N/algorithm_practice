# Tree (트리)

트리(Tree)는 계층적 구조를 가지는 비선형 자료구조 중 하나로, 노드(Node)들로 이루어져 있습니다. 트리는 루트(Root)라는 최상위 노드에서 시작하여 여러 자식 노드로 뻗어나가는 구조를 가지며, 각 노드는 여러 개의 자식 노드를 가질 수 있지만 하나의 부모 노드를 가집니다.


![예시 트리](https://file.notion.so/f/f/971703c5-12f6-4793-8670-fe9d2d59dbab/48115a41-5904-4455-a907-edec7fae7b65/Untitled.png?table=block&id=cd0512a0-0d4c-4c95-8ba0-f0bcc7d65bdd&spaceId=971703c5-12f6-4793-8670-fe9d2d59dbab&expirationTimestamp=1726128000000&signature=D-lVRBiA2nogRtbUhma34Qea7-ge3qs6k5xZjZIQayk&downloadName=Untitled.png)


트리는 다음과 같은 형태입니다.

## 트리 용어들

- **노드(Node) 혹은 버텍스(Vertex):** 트리의 구성요소 (A,B,C,D,E,F,G)
- **간선(Edge) 혹은 링크(Link):** 노드와 노드를 연결하는 연결선
- **루트 노드(Root Node):** 트리구조에서 최상위에 있는 노드 (A)
- **부모 노드 (Parent Node):** 특정노드와 연결되어 있는 윗 노드 (Ex - D의 부모노드는 B)
- **자식 노드 (Child Node):** 특정노드와 연결되어 있는 아래 노드 (Ex - B의 자식노드는 D, E)
- **형제 노드 (Sibling Node):** 같은 부모를 둔 노드 (Ex - D는 E와 형제 노드)
- **단말 노드 (Terminal Node), 잎사귀 노드(Leaf Node):** 아래로 다른 노드가 연결되어있지 않은 -노드
- **비단말 노드 (Nonterminal Node), 내부 노드 (Internal Node):** 아래로 다른 노드가 연결되어 있는 노드
- **레벨 (Level):** 각 계층을 숫자를 표현 (루트 노드가 0 레벨)
- **높이 (Height):** 트리 구조의 계층 길이 (A 의 높이는 3, B의 높이는 2, D의 높이는 1, H 높이는 1)

트리를 탐색하는 방식은 여러가지가 있습니다.

binary_tree.py 에는 그 예시들의 코드가 작성되어 있습니다.

## 트리 탐색

- **전위 순회** (Preorder Traversal)
![전위 순회](https://file.notion.so/f/f/971703c5-12f6-4793-8670-fe9d2d59dbab/5e1724e4-a7b9-4ad7-afcb-4ac0e7918ea8/Untitled.png?table=block&id=3f9f3c6a-0a1c-422a-a988-52dd20b5b337&spaceId=971703c5-12f6-4793-8670-fe9d2d59dbab&expirationTimestamp=1726128000000&signature=LwyPcqqY2fkunpM1lVwtNMRfYuplVidKSGMMl_m_nkA&downloadName=Untitled.png)

- **중위 순회** (Inorder Traversal)
![중위 순회](https://file.notion.so/f/f/971703c5-12f6-4793-8670-fe9d2d59dbab/d6f2e88e-6fa6-4634-b902-109c237064f2/Untitled.png?table=block&id=b62b7bdb-90da-49ef-8baf-e82a5c295b07&spaceId=971703c5-12f6-4793-8670-fe9d2d59dbab&expirationTimestamp=1726128000000&signature=x9i0dmhNy_VKAeNAx4y2iO-D4QLWoepsLzsR0TJOksw&downloadName=Untitled.png)

- **후위 순회** (Postorder Traversal)
![후위 순회](https://file.notion.so/f/f/971703c5-12f6-4793-8670-fe9d2d59dbab/2f55843c-e0e8-431d-9dd6-63f347f3317b/Untitled.png?table=block&id=b2f7f40a-38e8-4ce2-b0c5-d53f5e112539&spaceId=971703c5-12f6-4793-8670-fe9d2d59dbab&expirationTimestamp=1726128000000&signature=LLqJRGq9or2PFfqu-AMMfqNA8_t1KGb0QQoT-ZAXcEc&downloadName=Untitled.png)

- **레벨 순회** (Level Traversal) 혹은 **BFS**(Breadth-First Search)
![레벨 순회](https://file.notion.so/f/f/971703c5-12f6-4793-8670-fe9d2d59dbab/d045aa4a-d26a-404e-bb41-2240f7259565/Untitled.png?table=block&id=7c6e6050-32cc-49ec-a6f7-242fe66e43be&spaceId=971703c5-12f6-4793-8670-fe9d2d59dbab&expirationTimestamp=1726128000000&signature=UDUiGghxXKbglUXGiWr4H1ZZxym1ed5XFaZUEOUUH7c&downloadName=Untitled.png)
