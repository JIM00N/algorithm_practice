# Ploblem : [윤년] https://www.acmicpc.net/problem/2753
# Solver : 문지석 (jimoon@gachon.ac.kr)
# Solved Date : 2024.07.19
# BigO: 1

year = int(input())

if year%4 == 0:
    if (year%100!=0) or (year%400==0):
        print(1)
    else:
        print(0)
else:
    print(0)
