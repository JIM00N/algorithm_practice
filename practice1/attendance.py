# Ploblem : [과제 안 내신 분...?] https://www.acmicpc.net/problem/5597
# Solver : 문지석 (jimoon@gachon.ac.kr)
# Solved Date : 2024.07.19
# BigO: n

number = [n for n in range(1,31)]

for i in range(28):
    attended = int(input())
    number[attended - 1] = 0

number.sort(reverse=True)

print('{}\n{}'.format(number[1], number[0]))