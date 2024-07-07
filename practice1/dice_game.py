# Ploblem : [주사위 게임] https://www.acmicpc.net/problem/10103
# Solver : 문지석
# Solved Date : 2024.07.07
# BigO: n

chang, sang = 100, 100
n_round = int(input())

for i in range(n_round):
    c, s = input().split()
    c, s = int(c), int(s)
    if c > s:
        sang -= c
    elif c < s:
        chang -= s
    
print('{}\n{}'.format(chang, sang))