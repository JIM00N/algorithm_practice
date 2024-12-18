# Problem : [가장 긴 감소하는 부분 수열] https://www.acmicpc.net/problem/11722
# Solver : 문지석
# Solved Date : 2024.12.18
# BigO : n ** 2

def d_seq(n, seq):
    result = [1] * n
    for new_num_pos in range(n):
        for check_num_pos in range(new_num_pos):
            if seq[new_num_pos] < seq[check_num_pos]:
                result[new_num_pos] = max(result[new_num_pos], result[check_num_pos] + 1)

    return max(result)

if __name__=="__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    print(d_seq(n, seq))
