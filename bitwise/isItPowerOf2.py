# Problem : [2의 제곱인가?] https://www.acmicpc.net/problem/11966
# Solver : 문지석
# Solved Date : 2024.11.13
# BigO : log N


def isPower2(n):
    if n == 1: # n = 1이라면 바로 1 리턴
        return 1
    
    if n & 0x0001 == 0x0001: # 홀수라면 0 리턴
        return 0

    num_power2 = 0 # 제곱된 수가 하나만 있어야함
    while True:
        n = n >> 1
        if n == 0: # 종료조건, n이 0이 되었다면 종료
            return 1

        if n & 0x0001 == 0x1:
            num_power2 += 1
        
        if num_power2 == 2:
            return 0


if __name__=="__main__":
    n = int(input())
    print(isPower2(n))
