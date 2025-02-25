# Problem : [IP 주소] https://www.acmicpc.net/problem/2064
# Solver : 문지석
# Solved Date : 2025.02.25
# BigO : N
import sys


class IP:
    def __init__(self, data):
        self.mask = 0xFFFFFFFF
        self.num_common_bit = 0
        self.data = data

    def find_diff(self):
        ip_list = []
        for ip in self.data:
            tmp_ip = ip[0] << 24 | ip[1] << 16 | ip[2] << 8 | ip[3]
            ip_list.append(tmp_ip)

        max_ip = max(ip_list)
        min_ip = min(ip_list)

        diff_ip = max_ip ^ min_ip

        while diff_ip != 0:
            diff_ip >>= 1
            self.num_common_bit += 1

    def make_mask(self):
        self.mask >>= self.num_common_bit
        self.mask <<= self.num_common_bit

        sliced_mask = f"{(self.mask >> 24) & 0xff}.{(self.mask >> 16) & 0xff}.{(self.mask >> 8) & 0xff}.{self.mask & 0xff}"

        return sliced_mask

    def min_ip(self):
        tmp_ip = (
            self.data[0][0] << 24
            | self.data[0][1] << 16
            | self.data[0][2] << 8
            | self.data[0][3]
        )
        tmp_ip &= self.mask
        result_ip = ""
        for i in range(4):
            result_ip += f"{(tmp_ip >> (24 - 8 * i)) & 0xFF}."

        return result_ip.strip(".")


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    data = data[1:]
    data = [list(map(int, i.split("."))) for i in data]
    result = IP(data)
    result.find_diff()
    mask = result.make_mask()
    min_ip = result.min_ip()
    print(min_ip)
    print(mask)
