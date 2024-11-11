# Problem : [최소 힙] https://www.acmicpc.net/problem/1927
# Solver : 문지석
# Solved Date : 2024.11.11
# BigO :
import heapq
import sys


def min_heap(data):
    my_heap = []
    heapq.heapify(my_heap)

    for i in data[1:]:
        if i == 0:
            if len(my_heap) == 0:
                print(0)
            else:
                print(heapq.heappop(my_heap))

        else:
            heapq.heappush(my_heap, i)


if __name__ == "__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    min_heap(data)
