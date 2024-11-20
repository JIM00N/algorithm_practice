# Problem : [최단 경로] https://www.acmicpc.net/problem/1753
# Solver : 문지석
# Solved Date : 2024.11. 17
# BigO :


import heapq
import sys


def dijkstra(graph, start):
    visit = set()
    result = dict()
    p_queue = []
    p_queue.append(start)
    visit.add()

    while len(p_queue) != 0:  # BFS
        

    return result


if __name__ == "__main__":
    input = sys.stdin.read
    data = list(input().split("\n"))
    num_nodes, s_node = int(data[0][0]), int(data[1])
    
    paths = [[float("INF")] * 5 for x in range(5)]
    paths[0][0] = 1

    for path in data[2:]:
        if not path.strip():  # 빈 줄 무시
            continue
        u, v, w = tuple(map(int, path.split()))
        paths[u][v] = w

    print(dijkstra(paths, s_node))
