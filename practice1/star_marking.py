# Problem : [별 찍기 - 1] https://www.acmicpc.net/problem/2438
# Solver : 문지석
# Solved Date : 2024.07.07
# BigO : n

def star_marking(n):
    for i in range(n):
        print('*'*(i+1))
    
if __name__=="__main__":
    n = int(input())
    star_marking(n)