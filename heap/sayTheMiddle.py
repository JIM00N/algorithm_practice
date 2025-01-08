# Problem : [가운데를 말해요] https://www.acmicpc.net/problem/1655
# Solver : 문지석
# Solved Date : 2024.11.11
# BigO : 
import heapq
import sys

def searchTheMiddle(heap_len):
    if heap_len & 0x0001:
        return (heap_len - 1) >> 1
    else:
        return (heap_len >> 1) - 1

def sayTheMiddle(data):
    repitition = data[0] + 1
    data = data[1:]
    # heapq.heapify(data)
    for i in range(1, repitition):
        tmp_data = data[:i]
        heapq.heapify(tmp_data)
        for _ in range(searchTheMiddle(i)):
            heapq.heappop(tmp_data)

        print(tmp_data[0])


if __name__=="__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    sayTheMiddle(data)
