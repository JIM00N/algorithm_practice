import heapq


class MST:
    def __init__(self, num_nodes, weights, paths):
        self.num = num_nodes
        self.weight_heap = weights
        self.paths = paths
        self.mark_connected = {
            chr(97 + i): 0 for i in range(self.num)
        }  # 연결됨: 1, 안됨: 0
        self.weight_sum = 0 # 결과로 출력될 가중치의 합
        self.connected_nodes = 0 # 연결된 노드의 개수
        self.prior_q = []  # (weight, node)

    def initialize(self):
        # 가중치가 가장 낮은 경로에서 빨리오는 알파벳이 start node
        # 스타트 노드에 연결되어 있는 경로의 가중치와 노드를 heap에 저장
        start_node = self.weight_heap[0][1]
        for element in self.paths[start_node]:
            heapq.heappush(self.prior_q, element)
        self.paths[start_node] = []
        self.mark_connected[start_node] = 1
        self.connected_nodes += 1

    def connect(self):
        # 연결시키는 메인 메소드
        while self.is_all_connected() == 0:
            weight, next_node = heapq.heappop(self.prior_q)
            # 힙에서 가중치와 연결된 노드를 가져옴
            if self.mark_connected[next_node] == 1:
                # 연결된 노드라면 pass
                continue

            self.weight_sum += weight # 가중치 더하기
            self.mark_connected[next_node] = 1 # 연결 표시
            self.connected_nodes += 1 # 연결된 노드 개수 +1

            for element in self.paths[next_node]:
                if element[0] != weight:
                # 중복되는 값은 포함하지 않음
                    heapq.heappush(self.prior_q, element)

            self.paths[next_node] = []
            # 모두 heap에 넣었으니 비우기

    def is_all_connected(self):
        if self.connected_nodes == self.num:
            return 1
        else:
            return 0


if __name__ == "__main__":
    num_nodes, num_edges = tuple(map(int, input().split()))
    weight_edges_heap = []
    paths_dict = {chr(97 + i): [] for i in range(num_nodes)}

    for _ in range(num_edges):
        org, dst, weight = tuple(input().split())
        if dst < org:
            org, dst = dst, org
        heapq.heappush(paths_dict[org], (int(weight), dst))
        heapq.heappush(paths_dict[dst], (int(weight), org))
        weight_edges_heap.append((int(weight), org, dst))

    heapq.heapify(weight_edges_heap)
    mst = MST(num_nodes, weight_edges_heap, paths_dict)
    mst.initialize()
    mst.connect()
    print(mst.weight_sum)
