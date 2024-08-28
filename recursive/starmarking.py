# Problem : [별 찍기 - 10] https://www.acmicpc.net/problem/2447
# Solver : 문지석
# Solved Date : 2024.08.28
# BigO : 2 ** n
def erase_star(stars, x, y, n):
    if n==3:
        stars[x+1][y+1] = " "
    else:
        next_n = n//3
        
        # Row 1 - 1 | 2 | 3
        # Row 2 - 4 | 5 | 6
        # Row 3 - 7 | 8 | 9
        
        # Row 1 - 1 | 2 | 3
        erase_star(stars, x + (next_n * 0), y + (next_n * 0), next_n)
        erase_star(stars, x + (next_n * 1), y + (next_n * 0), next_n)
        erase_star(stars, x + (next_n * 2), y + (next_n * 0), next_n)
        
        # Row 2 - 4 | 5 | 6
        erase_star(stars, x + (next_n * 0), y + (next_n * 1), next_n)
        for i in range(x+next_n, x+(next_n*2)):
            for j in range(y+next_n, y+(2*next_n)):
                stars[i][j] = " "
        erase_star(stars, x + (next_n * 2), y + (next_n * 1), next_n)
        
        # Row 3 - 7 | 8 | 9
        erase_star(stars, x + (next_n * 0), y + (next_n * 2), next_n)
        erase_star(stars, x + (next_n * 1), y + (next_n * 2), next_n)
        erase_star(stars, x + (next_n * 2), y + (next_n * 2), next_n)

if __name__=="__main__":
    n = int(input())
    star_list = []
    for i in range(n):
        star_list.append(["*"] * n)
    erase_star(star_list, 0, 0, n)
    for i in range(n):
        for j in range(n):
            print(star_list[i][j], end="")
        print()
            