# Problem : [RGB거리] https://www.acmicpc.net/problem/1149
# Solver : 문지석
# Solved Date : 2025.01.03
# BigO : N

class RGB:
    def __init__(self, num_house, w_list):
        self.num = num_house
        self.weight = w_list
        self.val_list = [self.weight[0][0], self.weight[0][1], self.weight[0][2]]
        
    def cal_cost(self):
        for i in range(1, self.num):
            add_val_0 = min(self.val_list[1], self.val_list[2])
            add_val_1 = min(self.val_list[0], self.val_list[2])
            add_val_2 = min(self.val_list[0], self.val_list[1])
            self.val_list[0] = self.weight[i][0] + add_val_0
            self.val_list[1] = self.weight[i][1] + add_val_1
            self.val_list[2] = self.weight[i][2] + add_val_2


if __name__=="__main__":
    num_house = int(input())
    house_list = list()
    for i in range(num_house):
        house_list.append(list(map(int, input().split())))

    distance = RGB(num_house, house_list)
    distance.cal_cost()

    print(min(distance.val_list))
