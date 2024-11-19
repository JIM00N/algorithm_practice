# Problem : [최단 경로] https://www.acmicpc.net/problem/1753
# Solver : 문지석
# Solved Date : 2024.11. 17
# BigO : 


import heapq
import sys


def dijkstra(graph:dict, start):
    visit = set()
    result = {}
    p_queue = []

    # for node in list(graph.keys()): # 결과 초기화
    #     result[node] = float('INF') # infinity
    #     if node == start:
    #         visit.add(node)
    #         result[node] = 0
    #         heapq.heappush(p_queue, (result[start], start))

    while len(p_queue) != 0: # BFS
        cur_val, cur_key = heapq.heappop(p_queue)
        visit.add(cur_key)

        for key, value in graph[cur_key].items():
            new_val = value + cur_val
            result[key] = min(result[key], new_val)

        p_queue = []
        for key in graph:
            if key not in visit:
                heapq.heappush(p_queue, (result[key], key))

    return result


if __name__=="__main__":
    input = sys.stdin.read
    data = list(input().split('\n'))
    num_nodes, s_node = int(data[0][0]), int(data[1])

    path_dict = {key: {} for key in range(1, num_nodes + 1)} 
    for path in data[2:]:
        if not path.strip():  # 빈 줄 무시
            continue
        u, v, w = tuple(map(int, path.split()))
        if v in path_dict[u].keys() and w > path_dict[u][v]:
            continue    
        
        path_dict[u].update({v: w})
        
    for i in dijkstra(path_dict, s_node).values():
        if i == float("INF"):
            i = str(i).upper()
        print(i)
