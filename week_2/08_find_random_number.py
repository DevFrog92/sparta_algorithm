finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 이진 탐색의 경우 반드시 정렬이 되어 있어야 한다.
# 즉, 일정한 규칙 및 정렬이 되어 있는 데이터만 이진 탐색이 가능하다.
def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    # 버블정렬, 삽입정렬, 선택정렬, 퀵정렬 등을 활용하는 방법이 필요

    left = 0
    right = len(numbers)-1

    while left <= right:

        middle = (left+right)//2

        if numbers[middle] == target or numbers[left] == target or numbers[right] == target:
            return True
        if numbers[middle] > target:
            right = middle -1
        else:
            left = middle + 1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)