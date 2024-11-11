# Problem : [가운데를 말해요] https://www.acmicpc.net/problem/1655
# Solver : 문지석
# Solved Date : 2024.11.11
# BigO : 
import heapq
import sys
import copy


def searchTheMiddle(heap_len):
    if heap_len & 0x0001:
        return heap_len >> 1
    else:
        return (heap_len >> 1) - 1

def sayTheMiddle(heap, data): 
    repitition = data[0] + 1
    for idx in range(1, repitition):
        heapq.heappush(heap, data[idx])
        replicated_heap = copy.deepcopy(heap)
        for _ in range(searchTheMiddle(len(heap))):
            heapq.heappop(replicated_heap)

        print(replicated_heap[0])


if __name__=="__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    my_heap = []
    sayTheMiddle(my_heap, data)
