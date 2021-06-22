word = '가련하시다 사장 집 아들 딸들아 집 장사 다시 하련가'.replace(' ','')
def is_palindrome(word):

    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

result = is_palindrome(word)
print(result)