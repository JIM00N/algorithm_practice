# Ploblem : [쇠 막대기] https://www.acmicpc.net/problem/10799
# Solver : 문지석
# Solved Date : 2024.08.04
# BigO : 

brakets = input()
left = 0
piece = 0

for i in range(len(brakets)):
    if brakets[i]=='(':
        left += 1
    else:
        left -= 1
        if brakets[i-1]=='(':
            piece += left
        else:
            piece += 1

print(piece)