# Problem : [막대기] https://www.acmicpc.net/problem/1094
# Solver : 문지석
# Solved Date : 2024.11.13
# BigO : log N


def count(n):
    num_sticks = 0
    while n != 0:
        if n & 0x0001:
            num_sticks += 1
        
        n = n >> 1
    
    return num_sticks


if __name__=="__main__":
    x = int(input())
    print(count(x))
