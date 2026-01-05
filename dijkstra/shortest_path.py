# Problem : [최단 경로] https://www.acmicpc.net/problem/1753
# Solver : 문지석
# Solved Date : 2025.02.26
# BigO : VlogV+ElogV


import heapq
import sys

class Dijkstra:
    def __init__(self, data, start, num):
        self.data = data # dictionary {노드 번호: {도착 노드1: 소요 시간, 도착 노드2: 소요 시간...}}
        self.start = start # start node
        self.result_dict = {i+1 : float("INF") for i in range(num)} # initialize dict values as INF
        self.buffer = []
        self.visit = [False for _ in range(num)]

    def initialize_dict(self):
        self.result_dict[self.start] = 0 # start node has ZERO weight
        self.visit[self.start - 1] = True
        for dst, weight in self.data[self.start].items():
            # nodes connected with start node
            self.result_dict[dst] = min(self.result_dict[dst], weight)
            heapq.heappush(self.buffer, (weight, dst))
            # buffer is a heap to offer smaller weight path

    def path_finder(self):
        while self.buffer: # until there's no value in self.buffer
            org_weight, cur_node = heapq.heappop(self.buffer)
            if self.visit[cur_node - 1] == True: # if the node is visited, continue
                continue
            self.visit[cur_node - 1] = True
            self.result_dict[cur_node] = min(org_weight, self.result_dict[cur_node])

            for dst, tmp_weight in self.data[cur_node].items():
                total_weight = org_weight + tmp_weight # accumulate weights, from start node to next node
                if total_weight < self.result_dict[dst]:
                    heapq.heappush(self.buffer, (total_weight, dst))

if __name__ == "__main__":
    input = sys.stdin.read
    data = list(input().strip().split("\n"))
    num_nodes, s_node = int(data[0].split()[0]), int(data[1])
    
    data_dict = {i+1: {} for i in range(num_nodes)}
    # {노드 번호: {도착 노드1: 소요 시간, 도착 노드2: 소요 시간...}}
    for u_v_w in data[2:]:
        u_v_w = list(map(int, u_v_w.split()))
        u, v, w= u_v_w[0], u_v_w[1], u_v_w[2] #출발 노드, 도착 노드, 소요 시간
        try:
            # add min value only
            data_dict[u][v] = min(data_dict[u][v], w)
        except:
            # if there is no assigned value         
            data_dict[u][v] = w


    shortest_path = Dijkstra(data_dict, s_node, num_nodes)
    shortest_path.initialize_dict()
    shortest_path.path_finder()

    for weight in list(shortest_path.result_dict.values()):
        if weight == float("INF"):
            weight = "INF"
        print(weight)
