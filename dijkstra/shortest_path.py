# Problem : [최단 경로] https://www.acmicpc.net/problem/1753
# Solver : 문지석
# Solved Date : 2024.11. 17
# BigO :


import heapq
import sys

class Dijkstra:
    def __init__(self, data, start, num):
        self.data = data
        self.start = start
        self.result_dict = {i+1 : float("INF") for i in range(num)}
        self.buffer = []
        self.visit = [[False] for _ in range(num)]

    def path_finder(self):
        for idx, weight in enumerate(self.data[self.start - 1]):
            self.result_dict[idx + 1] = weight
            heapq.heappush(self.buffer, (weight, idx + 1)) #idx가 먼저일까 weight이 먼저일까
        
        while self.buffer or (False in self.visit):
            org_weight, tmp_node = heapq.heappop(self.buffer)
            self.visit[tmp_node - 1] = True
            for idx, tmp_weight in enumerate(self.data[tmp_node - 1]):
                if tmp_weight != 0 and tmp_weight != float("INF"):
                    add_weight = org_weight + tmp_weight
                    if self.result_dict[idx + 1] > add_weight:
                        self.result_dict[idx + 1] = add_weight
                        heapq.heappush(self.buffer, (add_weight, idx + 1))


if __name__ == "__main__":
    input = sys.stdin.read
    data = list(input().split("\n"))
    num_nodes, s_node = int(data[0].split()[0]), int(data[1])
    
    paths = [[float("INF")] * num_nodes for _ in range(num_nodes)]
    for idx in range(num_nodes):
        paths[idx][idx] = 0

    for path in data[2:]:
        if not path.strip():  # 빈 줄 무시
            continue
        u, v, w = tuple(map(int, path.split()))
        paths[u - 1][v - 1] = min(paths[u - 1][v - 1], w)
    
    
    shortest_path = Dijkstra(paths, s_node, num_nodes)
    shortest_path.path_finder()

    for weight in list(shortest_path.result_dict.values()):
        if weight == float("INF"):
            weight = "INF"
        print(weight)
