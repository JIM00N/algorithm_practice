# Problem : [IP 주소] https://www.acmicpc.net/problem/2064
# Solver : 문지석
# Solved Date : 2024.11.13
# BigO :
import sys


class IP:
    def __init__(self, data):
        self.data = data
        self.same = [True, True, True, True]
        self.mask = 0b11111111
        self.mutual_bit = 0b00000000
        self.num_m_bit = 0
        self.min_ip = [0, 0, 0, 0]
    
    def find_mutual_bit(self):
        try:
            aim_idx = self.same.index(False)
        except:
            self.min_ip = self.data[0]
            return
        count = 0
        for i in range(len(self.data)):
            if i == 0:
                self.mutual_bit = self.data[i][aim_idx]
                continue
            
            count -= count
            tmp_data = self.data[i][aim_idx]
            while self.mutual_bit != tmp_data:
                self.mutual_bit >>= 1
                tmp_data >>= 1
                count += 1
            self.num_m_bit = max(count, self.num_m_bit)
            self.mutual_bit <<= count


    def find_mask(self):
        try:
            aim_idx = self.same.index(False)
        except:
            self.mask = [255, 255, 255, 255]
            return
        self.mask >>= self.num_m_bit
        self.mask <<= self.num_m_bit
        result_mask = [255, 255, 255, 255]
        result_mask[aim_idx] = self.mask
        for i in range(aim_idx+1, 4):
            result_mask[i] = 0

        self.mask = result_mask
        
    def find_min_ip(self):
        try:
            aim_idx = self.same.index(False)
        except:
            return
        for idx, num in enumerate(data[0]):
            self.min_ip[idx] = self.mask[idx] & int(num)
            

    def diff_part(self):
        for idx in range(1, len(self.data)):
            if self.data[0][0] != self.data[idx][0]:
                self.same[0] = False
                break
            elif self.data[0][1] != self.data[idx][1]:
                self.same[1] = False
                break
            elif self.data[0][2] != self.data[idx][2]:
                self.same[2] = False
                break
            elif self.data[0][3] != self.data[idx][3]:
                self.same[3] = False
                break

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    data = data[1:]
    data = [list(map(int, i.split("."))) for i in data]
    result = IP(data)
    result.diff_part()
    result.find_mutual_bit()
    result.find_mask()
    result.find_min_ip()
    print(f"{result.min_ip[0]}.{result.min_ip[1]}.{result.min_ip[2]}.{result.min_ip[3]}")
    print(f"{result.mask[0]}.{result.mask[1]}.{result.mask[2]}.{result.mask[3]}")
