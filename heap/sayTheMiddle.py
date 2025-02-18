# Problem : [가운데를 말해요] https://www.acmicpc.net/problem/1655
# Solver : 문지석
# Solved Date : 2025.02.18
# BigO : N * log(N)
import heapq
import sys


def sayTheMiddle(data):
    repitition = data[0]
    data = data[1:]

    mid = data[0]
    smaller_heap = [] # max heap
    bigger_heap = [] # min heap

    for i in range(repitition):
        tmp_data = data[i]
        if tmp_data >= mid:
            heapq.heappush(bigger_heap, tmp_data)
        else:
            heapq.heappush(smaller_heap, (-1) * tmp_data)
        
        gap = len(smaller_heap) - len(bigger_heap)
        
        if gap == 0 or gap == 1:
            mid = smaller_heap[0] * (-1)
            print(mid)
        elif gap == -1:
            mid = heapq.heappop(bigger_heap)
            heapq.heappush(smaller_heap, (-1) * mid)
            print(mid)
        elif gap == 2:
            transfer = heapq.heappop(smaller_heap)
            heapq.heappush(bigger_heap, (-1) * transfer)
            mid = smaller_heap[0] * (-1)
            print(mid)

if __name__=="__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    sayTheMiddle(data)
