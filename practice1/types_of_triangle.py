# Problem : [삼각형 외우기] https://www.acmicpc.net/problem/10101
# Solver : 문지석
# Solved Date : 2024.07.20
# BigO : n

angles = [int(input()) for i in range(3)]

angles.sort()

if (angles[0] + angles[1] + angles[2]) == 180:
    if angles[0]==angles[2]:
        print('Equilateral')
    elif angles[0]==angles[1] or angles[1]==angles[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
