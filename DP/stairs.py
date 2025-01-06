# Problem : [계단 오르기] https://www.acmicpc.net/problem/2579
# Solver : 문지석
# Solved Date : 2025.01.06
# BigO : n


def max_score(stairs):
    if len(stairs) == 2:
        return stairs[0] + stairs[1]
    elif len(stairs) == 1:
        return stairs[0]

    scores = []
    scores.append([stairs[0], stairs[0]])
    scores.append([stairs[0] + stairs[1], stairs[1]])

    idx = 2
    while len(scores) != len(stairs):
        o_prev = scores[idx - 1][-1] + stairs[idx]
        x_prev = max(scores[idx - 2]) + stairs[idx]
        scores.append([o_prev, x_prev])
        idx += 1

    return max(scores[-1])


if __name__ == "__main__":
    num_stairs = int(input())
    stairs = [int(input()) for _ in range(num_stairs)]
    print(max_score(stairs))
