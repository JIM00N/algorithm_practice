# Problem : [별 찍기 - 10] https://www.acmicpc.net/problem/2447
# Solver : 문지석
# Solved Date : 2024.08.16
# BigO : 2 ** n


class star_marking_10:
    def __init__(self, n):
        self.n = n
        # mid는 별찍기 중간부분 star_marked는 기본 구조를 가진다.
        self.mid = "*" + self.blank(1) + "*"
        self.star_marked = "***" + "\n" + self.mid + "\n" + "***"
        self.count = 1

    def star_marking(self, n):
        if n == 3:
            return self.star_marked
        else:
            self.mid = self.multi_mid(3**self.count)
            self.count += 1
            # 재귀를 사용했기에 처음부터 중간부분을 완성형으로 만들기보다 호출될 때마다 중간부분을 키워준다.
            top_bottom = self.three_times(self.star_marked)
            # 이전 전체 구조를 세배해서 위아래를 덮어주기
            self.star_marked = top_bottom + "\n" + self.mid + "\n" + top_bottom
            return self.star_marking(n // 3)

    def blank(self, n):
        bl = " " * n
        return bl

    def three_times(self, stars):
        # 세배로 만들기 "***\n* *" ->"*********\n* ** ** *"
        strs = ""
        strs_long = ""
        for i in stars:
            if i == "\n":
                # 줄 바꿈이 나오면 앞에서 더해준 스트링을 세배하고 줄바꿈 추가한 뒤 스트링 최기화
                strs_long += 3 * strs + i
                strs = ""
            else:
                # 줄 바꿈이 나오기 전에 빈 스트링에 더하기
                strs += i
        # 마지막에는 줄 바꿈이 없으니 그냥 세배해서 더하기
        strs_long += 3 * strs
        return strs_long

    def multi_mid(self, k):
        # self.mid를 "* *"에서 "***   ***\n* *   * *\n***   ***" 이렇게 바꾸어주는 함수
        element = self.star_marked
        # n이 커질 때 이전의 전체는 다음의 일부가 된다.
        mul_mid = ""
        tmp = ""
        for i in element:
            if i == "\n":
                tmp = tmp + self.blank(k) + tmp + i
                mul_mid += tmp
                tmp = ""

            else:
                tmp += i
        mul_mid += tmp + self.blank(k) + tmp
        return mul_mid


n = int(input())
stars = star_marking_10(n)
result = stars.star_marking(stars.n)
print(result)
