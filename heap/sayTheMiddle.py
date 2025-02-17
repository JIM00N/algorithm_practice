# Problem : [가운데를 말해요] https://www.acmicpc.net/problem/1655
# Solver : 문지석
# Solved Date : 2025.02.17
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

    for i in range(1, repitition):
        tmp_data = data[:i]
        n = searchTheMiddle(i)
        result = heapq.nsmallest(n + 1, tmp_data)
        print(result[-1])


if __name__=="__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    sayTheMiddle(data)
