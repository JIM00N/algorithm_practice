# Ploblem : [사칙연산] https://www.acmicpc.net/problem/1316
# Solver : 문지석 (jimoon@gachon.ac.kr)
# Solved Date : 2024.07.19
# BigO: n ** 2

n = int(input())
words = [] # 입력 단어들
count = n # 출력될 값 초기값을 n으로 한 뒤, 해당하지 않는 단어 개수 빼기

for i in range(n):
    word = input()
    words.append(word)
#단어 입력

for word in words:
    characters = {} 
    # 딕셔너리를 이용하여 {'char' : idx}의 형태로 저장
    for idx, char in enumerate(word):
    # enumerate으로 인덱스 값과 해당하는 알파벳을 같이 가져오자        
        if char in characters:
        # 알파벳이 이미 딕셔너리에 포함되어 있다면
            if idx - characters[char] == 1:
            # 연속한 같은 알파벳인지 확인
                characters[char] = idx
            else:
                count -= 1 
                # 그룹 단어 아닌 단어 개수 빼기
                break
        else:
        # 딕셔너리에 없는 알파벳이라면 추가
            characters[char] = idx

print(count)
