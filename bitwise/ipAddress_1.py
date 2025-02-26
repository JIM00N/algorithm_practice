# Problem : [IP 주소] https://www.acmicpc.net/problem/2064
# Solver : 문지석
# Solved Date : 2024.02.25
# BigO : N
import sys


class IP:
    def __init__(self, data):
        self.data = data
        # ip주소를 [[x_1, x_2, x_3, x_4], [y_1, y_2, y_3, y_4]..]형태로 받음
        self.is_same = [True, True, True, True]
        # 달라지는 부분을 표시하기 위함 x_3 != y_3 이면 [True, True, False, True]
        self.mask = 0b11111111
        # is_same에서 가장 앞의 False에 해당하는 mask
        self.common_bit = 0b00000000
        # 1010 & 1011 이 있다면 공통 부분을 포함하고 다른 부분은 0으로 표시하여 1010이 됨
        self.num_diff_bit = 0
        # 1010 & 1011 이 있다면 다른 비트는 하나이므로 self.num_diff_bit == 1
        self.min_ip = [0, 0, 0, 0]
        # 최소 ip를 "." 기준으로 나누어서 저장

    def diff_part(self):
        for idx in range(1, len(self.data)):
            if self.data[0][0] != self.data[idx][0]:
                self.is_same[0] = False
            elif self.data[0][1] != self.data[idx][1]:
                self.is_same[1] = False
            elif self.data[0][2] != self.data[idx][2]:
                self.is_same[2] = False
            elif self.data[0][3] != self.data[idx][3]:
                self.is_same[3] = False

    def find_common_bit(self):
        try:
            # 입력이 하나라 is_same에 false가 없는 경우를 예외처리
            # false가 처음으로 나오는 자리부터 ip가 달라진다.
            aim_idx = self.is_same.index(False)
        except:
            self.min_ip = self.data[0]
            # 입력이 하나이면 그 입력 자체가 min_ip
            return

        for i in range(len(self.data)):
            """_summary_
            1. 첫 입력을 공통비트로 설정
            2. 다음 입력을 공통비트와 함께 같아질 때까지 >> 연산 + 연산횟수 세기
            3. 연산횟수 == 서로 다른 비트 수
            4. 가장 많은 연산 횟수 == 다른 비트 수
            5. 줄어든 common_bit를 원래 길이로 복원
            """
            if i == 0:
                self.common_bit = self.data[i][aim_idx]
                continue

            count = 0
            tmp_data = self.data[i][aim_idx]
            while self.common_bit != tmp_data:
                self.common_bit >>= 1
                tmp_data >>= 1
                count += 1
            self.num_diff_bit = max(count, self.num_diff_bit)
            self.common_bit <<= count

    def find_mask(self):
        try:
            aim_idx = self.is_same.index(False)
        except:
            # 입력이 하나라면 mask는 255.255.255.255
            self.mask = [255, 255, 255, 255]
            return
        """_summary_
        1. 다른 비트 수 만큼 mask의 비트를 0으로 만들어줌
        2. 필요한 위치에 mask 입력
        3. 그 위치보다 뒤는 모두 0으로 채움
        """
        self.mask >>= self.num_diff_bit
        self.mask <<= self.num_diff_bit
        result_mask = [255, 255, 255, 255]
        result_mask[aim_idx] = self.mask
        for i in range(aim_idx + 1, 4):
            result_mask[i] = 0

        self.mask = result_mask

    def find_min_ip(self):
        # 최소 ip는 어떤 ip에 mask와 AND 연산한 것
        try:
            aim_idx = self.is_same.index(False)
        except:
            return
        for idx, num in enumerate(data[0]):
            self.min_ip[idx] = self.mask[idx] & num


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    data = data[1:]
    data = [list(map(int, i.split("."))) for i in data]
    result = IP(data)
    result.diff_part()
    result.find_common_bit()
    result.find_mask()
    result.find_min_ip()
    print(
        f"{result.min_ip[0]}.{result.min_ip[1]}.{result.min_ip[2]}.{result.min_ip[3]}"
    )
    print(f"{result.mask[0]}.{result.mask[1]}.{result.mask[2]}.{result.mask[3]}")
