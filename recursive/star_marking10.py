# Problem : [별 찍기 - 10] https://www.acmicpc.net/problem/2447
# Solver : 문지석
# Solved Date : 2024.08.16
# BigO : 2 ** n

class star_marking_10():
    def __init__(self, n):
        self.n = n
        self.star_list = ["*", "***"]
        self.a = f"{self.star_list[0]}" + self.blank(1) + f"{self.star_list[0]}"
        self.star_marked = self.star_list[1] + "\n" + self.a + "\n" + self.star_list[1]
        self.count = 1
    def star_marking(self, n):
        if n==3:
            return self.star_marked
        else:
            mul_a = self.multi_a(3**self.count)
            self.count += 1
            self.star_marked = self.threeTimes_1(self.star_marked) + "\n" + mul_a + "\n" + self.threeTimes_1(self.star_marked)
            return self.star_marking(n//3)

    def blank(self, n):
        bl = ' '*n
        return bl

    def threeTimes_1(self, stars):
        strs = ""
        strs_long = ""
        for i in stars:
            if i=="\n":
                strs_long += (3*strs + i)
                strs = ""
            else:
                strs += i
        
        strs_long += 3*strs
        return strs_long
        
    def threeTimes_2(self, stars):
        strs = ""
        for i in stars:
            if i=="\n":
                continue
            else:
                strs += i*3
        
        return strs
    
    def multi_a(self, k):
        self.a = self.star_marked
        mul_a = ""
        tmp = ""
        for i in self.a:
            if i=="\n":
                tmp = tmp + self.blank(k) + tmp + i
                mul_a += tmp
                tmp = ""

            else:
                tmp += i
        mul_a += tmp + self.blank(k) + tmp
        return mul_a

n = int(input())
stars = star_marking_10(n)
result = stars.star_marking(stars.n)
print(result)
