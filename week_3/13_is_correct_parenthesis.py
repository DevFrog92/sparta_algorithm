def is_correct_parenthesis(string):
    s = list(string)
    stack = []

    if len(s)%2:
        return False

    for i in range(len(s)):
        value = s.pop()
        if stack:
            stack[-1] != s
            stack.pop()
        else:
            stack.append(value)
    if stack:
        return False
    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))