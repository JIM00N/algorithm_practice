# Ploblem : [칸토어 집합] https://www.acmicpc.net/problem/4779
# Solver : 문지석
# Solved Date : 2024.09.02
# BigO : 2 ** n


def cantor(line, n, start, end):
    sep_1 = int(end / 3)
    sep_2 = 2 * sep_1
    
    if n == 0:
        return line

    else:
        # line = --1-- | --2-- | --3--

        # --1--
        num_1 = cantor(line[:sep_1], n - 1, start, sep_1)

        # --2--
        # replace - to blank in the middle of the line
        num_2 = line[sep_1:sep_2].replace("-", " ")

        # --3-- 대칭
        num_3 = num_1

        return num_1 + num_2 + num_3


while True:
    try:
        n = int(input())
        line = "-"*(3**n)
        start = 0
        end = len(line)

    except:
        break

    print(f"{cantor(line, n ,start, end)}")
