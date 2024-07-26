# Problem : [삼각형 외우기] https://www.acmicpc.net/problem/10101
# Solver : 문지석
# Solved Date : 2024.07.20
# BigO : n log n (sort)

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

'''
# 멘토님의 풀이

triangles = {
    1 : 'Equilateral',
    2 : 'Isosceles',
    3 : 'Scalene'
}

angles = [int(input()) for i in range(3)]
print(triangles[len(set(angles)) if sum(angles) == 180 else "Error"])

# trianles에는 서로 다른 각의 개수에 따라 삼각형을 분류해두고
# set을 사용하여 서로 다른 값들만 남긴다. 그 값들의 개수가 삼각형을 결정한다.
# 그리고 모든 각들을 더하고 180이 되지 않는다면 Error을 출력한다.
'''
