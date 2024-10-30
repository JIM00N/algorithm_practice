# Problem : [계단 오르기] https://www.acmicpc.net/problem/2579
# Solver : 문지석
# Solved Date : 2024.10.06
# BigO : n

# def num_step(n):
#     step_count = [1, 2, 2]
#     if n <= 3:
#         return step_count[n-1]
#     for i in range(4, n+1):
#         if i % 3 == 1:
#             step_count.append(step_count[i - 2] + 1)
#         elif i % 3 == 2:
#             step_count.append(step_count[i - 3] + 2)
#         else:
#             step_count.append(step_count[-1])
    
#     return step_count[-1]
            
def max_score(score_list):
    length = len(score_list)
    # steps = num_step(length)
    

if __name__=="__main__":
    num_stairs = int(input())
    scores = [int(input()) for _ in range(num_stairs)]


'''
n = 
1) n - 2 
2) n - 1 +>> n - 3
dp를 사용하려면 리스트 두개를 만들고 서로 더해가자 n-2와 n-3을 두개 같이 계산하면 안돼
'''