numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(sum_value,array, target):
    answer = 0
    if sum(sum_value) == target and len(sum_value) == len(numbers):
        return 1
    for index in range(len(array)):
        if index < len(array):
            answer += get_count_of_ways_to_target_by_doing_plus_or_minus(sum_value+[array[index]], array[index + 1:], target)
            answer += get_count_of_ways_to_target_by_doing_plus_or_minus(sum_value+[-1*array[index]], array[index + 1:], target)
    return answer

print(get_count_of_ways_to_target_by_doing_plus_or_minus([],numbers, target_number))  # 5를 반환해야 합니다!
