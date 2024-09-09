# Ploblem : [카드2] https://www.acmicpc.net/problem/2164
# Solver : 문지석 (jimoon@gachon.ac.kr)
# Solved Date : 2024.08.04
# BigO: n
from collections import deque
n = int(input())

queue = deque()
for i in range(n):
    queue.append(i+1)
    
while len(queue)!=1:
    queue.popleft()
    queue.append(queue.popleft())


print(queue[0])
