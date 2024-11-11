# Problem : [최대 힙] https://www.acmicpc.net/problem/11279
# Solver : 문지석
# Solved Date : 2024.11.11
# BigO: N * logN
import heapq
import sys

input = sys.stdin.read
data = list(map(int, input().split()))
max_heap = []
heapq.heapify(max_heap)

for i in range(1, data[0] + 1):
    operator = data[i]
    if operator == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            a = heapq.heappop(max_heap)
            print(-1 * a)
    
    else:
        heapq.heappush(max_heap, -1 * operator)
