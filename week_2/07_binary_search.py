finding_target = 14
finding_numbers = [i for i in range(1,18)]

def id_existing_target_number_in_binary(target,array):
    left = 0
    right = len(array)-1
    count = 0
    while left <= right:
        middle = (left+right)//2
        count +=1
        if array[middle] == target or array[left] == target or array[right] == target:
            print(count)
            return True

        if array[middle] > target:
            right = middle-1
        else:
            left = middle+1
    print(count)
    return False

result = id_existing_target_number_in_binary(finding_target,finding_numbers)
print(result)
