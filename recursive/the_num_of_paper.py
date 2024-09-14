# Problem : [종이의 개수] https://www.acmicpc.net/problem/1780
# Solver : 문지석
# Solved Date : 2024.09.08
# BigO : n ** 2 


def papers(matrix : list, result : list, size : int, row=0, col=0):
    only_one = True
    tmp = 0
    for i in range(row, row + size):
        for j in range(col, col + size):
            if i == row and j == col:
                tmp = matrix[i][j]

            if tmp != matrix[i][j]:
                only_one = False
                break

        if only_one == False:
            break
            
    
    if only_one == True:
        if tmp == -1:
            result[0] += 1
        elif tmp == 0:
            result[1] += 1
        elif tmp == 1:
            result[2] += 1

    else:
        # -1- -2- -3-
        # -4- -5- -6-
        # -7- -8- -9-
        size = int(size/3)
        
        # -1- -2- -3-
        papers(matrix, result, size, row, col)
        papers(matrix, result, size, row, col + size)
        papers(matrix, result, size, row, col + size*2)
        # -4- -5- -6-
        papers(matrix, result, size, row + size, col)
        papers(matrix, result, size, row + size, col + size)
        papers(matrix, result, size, row + size, col + size*2)
        # -7- -8- -9-
        papers(matrix, result, size, row + size*2, col)
        papers(matrix, result, size, row + size*2, col + size)
        papers(matrix, result, size, row + size*2, col + size*2)


sides = int(input())
paper_matrix = []

for _ in range(sides):
    paper_matrix.append(list(map(int,input().split())))

# the number of each integers -1, 0, 1
result_list = [0, 0, 0]

papers(paper_matrix, result_list, sides)

for i in range(3):
    print(result_list[i])
