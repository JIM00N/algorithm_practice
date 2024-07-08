# Ploblem : [알파벳 찾기] https://www.acmicpc.net/problem/10809
# Solver : 문지석
# Solved Date : 2024.07.08
# BigO : n 
import string
alphabets = list(string.ascii_lowercase)

def alphabet_searching(word):
    idx = ""
    for chr in alphabets:
        if chr in word:
            chr_idx = word.find(chr)
            idx += '{} '.format(chr_idx)
        else:
            idx += '-1 '
    print(idx)

if __name__ == "__main__":
    word = input()
    alphabet_searching(word)
    