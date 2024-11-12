# Problem : [카드 정렬하기] https://www.acmicpc.net/problem/1715
# Solver : 문지석
# Solved Date : 2024.11.12
# BigO : N * logN
import heapq
import sys


def min_compare(repitition, decks):
    sum_list = []

    if len(decks) == 1:
        heapq.heappop(decks)
        sum_list.append(0)

    while len(decks) != 0:
        if len(sum_list) == 0:
            val_add = heapq.heappop(decks) + heapq.heappop(decks)
            sum_list.append(val_add)
        else:
            if sum_list[-1] > decks[0]:
                heapq.heappush(decks, sum_list[-1])
                val_add = heapq.heappop(decks) + heapq.heappop(decks)
                sum_list.append(val_add)
            else:
                sum_list.append(sum_list[-1] + heapq.heappop(decks))

    return sum(sum_list)


if __name__ == "__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    data_heap = data[1:]
    heapq.heapify(data_heap)
    print(min_compare(data[0], data_heap))
