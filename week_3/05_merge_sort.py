array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array)<=1:
        return array

    mid = (0+len(array))//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left,right)


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


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

# array1과 array2의 길이 만큼만 시간이 걸리게 된다.
# merge o(N) 각 길이를 반으로 쪼갰기 때문에
# O(n/2) + O(n/2) = O(n)

# [1,2,3,4,5,6,7,8] 길이가 N이다.
# [1,2,3,5] [4,6,7,8] 길이가 N/2 2개 비교하면서 합친다. 즉 N 만큼 합치게 된다.

# [3,5] [1,2] -> [1,2,3,5] 길이 N/4 2개
# [6,8] [4,7] -> [4,6,7,8]

# 즉, k단계만큼 반복하는게 각각 단계에서는 O(N)의 시간 복잡도가 걸린다.
# 즉, 분할정복의 O(logN)에 각 시간 복잡도 O(N)이 걸리게 되므로,
# 합병 정렬의 시간 복잡도는 O(NlogN)이 된다.