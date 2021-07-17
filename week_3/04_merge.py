array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    answer = []
    n = len(array1)
    m = len(array2)
    left,right = 0,0

    while left < n and right < m:
        if array1[left] < array2[right]:
            answer.append(array1[left])
            left+=1
        else:
            answer.append(array2[right])
            right += 1
    if left == n:
        answer += array2[right:]
    else:
        answer += array1[left:]
    return answer


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!