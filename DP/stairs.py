# Problem : [계단 오르기] https://www.acmicpc.net/problem/2579
# Solver : 문지석
# Solved Date : 2024.10.06
# BigO : n


# def path(n):
#     paths_dict = {1: 1, 2: 1, 3: 2, 4: 2}
#     for i in range(5, n+1):
#         tmp = paths_dict[i - 2] + paths_dict[i - 3]
#         paths_dict[i] = tmp

#     return paths_dict[n]

def max_score(score_list):
    pass
    
    

if __name__=="__main__":
    num_stairs = int(input())
    scores = [int(input()) for _ in range(num_stairs)]
    # paths = path(num_stairs)
    # print(max_score(paths, scores))
    # print(path(num_stairs))

'''
n = 
1) n - 2 
2) n - 1 +>> n - 3
dp를 사용하려면 리스트 두개를 만들고 서로 더해가자 n-2와 n-3을 두개 같이 계산하면 안돼
'''