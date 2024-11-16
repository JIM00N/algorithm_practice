import heapq

def dijkstra(graph:dict, start):
    visit = {}
    result = {}
    p_queue = []

    for node in list(graph.keys()): # 결과 초기화
        result[node] = float('INF') # infinity
        visit[node] = False
        if node == start:
            result[node] = 0
            heapq.heappush(p_queue, (result[start], start))

    while len(p_queue) != 0:
        cur_val, cur_key = heapq.heappop(p_queue)
        visit[cur_key] = True

        for key, value in graph[cur_key].items():
            new_val = value + cur_val
            result[key] = min(result[key], new_val)

        p_queue = []
        for key in graph.keys():
            if visit[key] == False:
                heapq.heappush(p_queue, (result[key], key))
    
    return result


if __name__=="__main__":
    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }
    
    print(dijkstra(graph, 'A'))

# {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}