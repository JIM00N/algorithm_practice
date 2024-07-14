# Ploblem : [검증수] https://www.acmicpc.net/problem/2475
# Solver : 문지석 (jimoon@gachon.ac.kr)
# Solved Date : 2024.07.09
# BigO: n

serial_number = input().split()

squared = (int(a)**2 for a in serial_number)
sum_squared = 0

for i in squared:
    sum_squared += i

print(sum_squared%10)
