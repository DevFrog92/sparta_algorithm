input = [3, 5, 6, 1, 2, 4]


def findMaxNumber(array):
    answer = array[0]
    for i in array:
        if answer < i:
            answer = i
    return answer


def find_max_number(array):
    for num in array:
        for compare_num in array:
            if num < compare_num: break
        else:
            return num


result = findMaxNumber(input)
result2 = find_max_number(input)
print(result, result2)
