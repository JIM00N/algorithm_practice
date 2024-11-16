# Problem : [IP 주소] https://www.acmicpc.net/problem/2064
# Solver : 문지석
# Solved Date : 2024.11.13
# BigO :
import sys


def compare_not_xor(front, end):
    val = 0
    count = 0  # 2 ** count keep being added to val
    for _ in range(8):
        if front & 0x0001 == end & 0x0001:
            val += 2**count

        count += 1

        front, end = front >> 1, end >> 1

    return val


def compare_1_1(front, end):
    val = 0
    count = 0  # 2 ** count keep being added to val
    while front != 0 or end != 0:
        if front & 0b1 == end & 0b1:
            val += 2**count * (front & 0b1)

        count += 1
        front, end = front >> 1, end >> 1

    return val


def mask(n, networks):  # 0이든 1이든 모두 같은 거라면 1 다르면 0 xor 반대임
    idx_0, idx_1 = networks[0][0], networks[0][1]
    idx_2, idx_3 = networks[0][2], networks[0][3]
    seperated_ip = [255, 255, 255, 255]
    for i in range(1, n):
        if i == 1:
            seperated_ip[0] = compare_not_xor(idx_0, networks[i][0])
            seperated_ip[1] = compare_not_xor(idx_1, networks[i][1])
            seperated_ip[2] = compare_not_xor(idx_2, networks[i][2])
            seperated_ip[3] = compare_not_xor(idx_3, networks[i][3])

        else:
            seperated_ip[0] = compare_1_1(
                seperated_ip[0], compare_not_xor(idx_0, networks[i][0])
            )
            seperated_ip[1] = compare_1_1(
                seperated_ip[1], compare_not_xor(idx_1, networks[i][1])
            )
            seperated_ip[2] = compare_1_1(
                seperated_ip[2], compare_not_xor(idx_2, networks[i][2])
            )
            seperated_ip[3] = compare_1_1(
                seperated_ip[3], compare_not_xor(idx_3, networks[i][3])
            )

        idx_0 = networks[i][0]
        idx_1 = networks[i][1]
        idx_2 = networks[i][2]
        idx_3 = networks[i][3]

    print(seperated_ip)


def IPaddress(n, networks):  # 1로 모두 같으면 1
    idx_0, idx_1 = networks[0][0], networks[0][1]
    idx_2, idx_3 = networks[0][2], networks[0][3]
    seperated_ip = [idx_0, idx_1, idx_2, idx_3]
    for i in range(1, n):
        if i == 1:
            seperated_ip[0] = compare_1_1(idx_0, networks[i][0])
            seperated_ip[1] = compare_1_1(idx_1, networks[i][1])
            seperated_ip[2] = compare_1_1(idx_2, networks[i][2])
            seperated_ip[3] = compare_1_1(idx_3, networks[i][3])

        else:
            seperated_ip[0] = compare_1_1(
                seperated_ip[0], compare_1_1(idx_0, networks[i][0])
            )
            seperated_ip[1] = compare_1_1(
                seperated_ip[1], compare_1_1(idx_1, networks[i][1])
            )
            seperated_ip[2] = compare_1_1(
                seperated_ip[2], compare_1_1(idx_2, networks[i][2])
            )
            seperated_ip[3] = compare_1_1(
                seperated_ip[3], compare_1_1(idx_3, networks[i][3])
            )

        idx_0 = networks[i][0]
        idx_1 = networks[i][1]
        idx_2 = networks[i][2]
        idx_3 = networks[i][3]

    print(seperated_ip)


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    data = data[1:]
    data = [tuple(map(int, i.split("."))) for i in data]
    IPaddress(n, data)
    mask(n, data)
