# Problem : [카드 정렬하기] https://www.acmicpc.net/problem/1715
# Solver : 문지석
# Solved Date : 2024.11.12
# BigO : N * logN
import heapq
import sys


def min_compare(repitition, decks):
    sum_list = []

    if len(decks) == 1:# 카드 뭉치가 하나라면 비교할 필요가 없음 따라서 0 추가
        heapq.heappop(decks) # while을 거치지 않도록 pop
        sum_list.append(0)

    while len(decks) != 0:
        if len(sum_list) == 0:
            val_add = heapq.heappop(decks) + heapq.heappop(decks)
            sum_list.append(val_add)
        else:
            if sum_list[-1] > decks[0]: # 두개를 더 했을 때 다음에 더할 카드보다 크다면
                heapq.heappush(decks, sum_list[-1]) # 다시 더할 카드 목록에 추가
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
