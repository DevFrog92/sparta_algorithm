input = "abacabade"

# 반복되는 것을 찾는 문자에서는 어떻게 반복되는 것을 저장할지 생각해야 한다.
# 빈도수를 저장하는 저장소에 대한 생각을 해야한다.
# 기존 문자열의 순서를 보장해 주는가? 생각해 봐야 한다.

def find_not_repeating_character(string):
    ascii = [0]*100
    for char in string: # n 번 연산
        ascii[ord(char)-ord('a')] += 1 # 덧셈 연산

    for index in range(len(string)): # n번 연산
        if ascii[ord(string[index])-ord('a')] == 1:
            result = string[index]
            break
    else:
        result = '_'

    # N + N번 연산 = O(N)의 시간 복잡도도
    return result


print("정답 = d 현재 풀이 값 =", find_not_repeating_character("abadabac"))
print("정답 = c 현재 풀이 값 =", find_not_repeating_character("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", find_not_repeating_character("aaaaaaaa"))