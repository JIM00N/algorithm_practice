# Maximal Flow, Edmonds-Karp Algorithm


class Edmonds_Karp:
    def __init__(self, src_sink: tuple, edges: dict):
        self.q = []  # Queue for BFS
        self.total_flow = 0

        self.src, self.sink = src_sink
        self.edges = edges
        self.min_flow = float("INF")

        self.parent = [-1] * len(edges)
        # 부모 노드 번호 저장
        self.visit = [False] * len(edges)
        # 방문 여부

    def bfs_forward(self):
        self.parent = [-1] * len(edges)
        self.visit = [False] * len(edges)
        self.q = [self.src]

        self.parent[self.src - 1] = self.src
        self.visit[self.src - 1] = True

        while self.q:
            cur_node = self.q.pop(0)
            if cur_node == self.sink:
                self.find_min_flow()
                return True

            for i in self.edges[cur_node]:
                capa, f_flow, _ = edges[cur_node][i]
                residual_capacity = capa - f_flow
                if residual_capacity > 0 and not self.visit[i - 1]:
                    self.q.append(i)
                    self.visit[i - 1] = True
                    self.parent[i - 1] = cur_node

        return False

    def find_min_flow(self):
        path = []
        next_node = self.sink
        prev_node = self.parent[self.sink - 1]

        while next_node != prev_node:  # (경로 + 최소유량) 찾기
            # 1번 노드의 부모는 1번으로 설정했으니 next와 prev가 같다면 마무리: 1 -> 3 에서 next=3이고 prev=가 1인 상황
            path.append(next_node)
            residual_capacity = (
                self.edges[prev_node][next_node][0]
                - self.edges[prev_node][next_node][1]
            )
            # residual_capacity = capacity - current_flow
            self.min_flow = min(self.min_flow, residual_capacity)
            prev_node, next_node = self.parent[prev_node - 1], prev_node
            # 부모 노드로 교체
            # parent 리스트엔 인덱스로 접근해야하니 prev - 1

        path.append(next_node)
        path.reverse()

        for i in range(len(path) - 1):
            self.edges[path[i]][path[i + 1]][1] += self.min_flow
            self.edges[path[i]][path[i + 1]][2] -= self.min_flow

        self.total_flow += self.min_flow
        self.min_flow = float("INF")


if __name__ == "__main__":
    v, e = tuple(map(int, input().split()))
    src, snc = tuple(map(int, input().split()))
    edges = {i: {j: [0, 0, 0] for j in range(1, v + 1)} for i in range(1, v + 1)}
    # [{capacity}, {forward}, {backward}]
    for _ in range(e):
        source, sink, capa = tuple(map(int, input().split()))
        edges[source][sink][0] = capa

    maximal_flow = Edmonds_Karp((src, snc), edges)
    while maximal_flow.bfs_forward() == True:
        pass

    print(maximal_flow.edges)
    print(maximal_flow.total_flow)
