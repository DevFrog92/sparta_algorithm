input = [4, 6, 2, 9, 1]


def insertion_sort(array):

    n = len(array)

    for i in range(1,n):
        min_index = i
        for j in range(i-1,-1,-1):
            if array[min_index] < array[j]:
                array[min_index],array[j] = array[j],array[min_index]
                min_index = j
    return array


def insertion_sort2(array):
    n = len(array)
    for i in range(1,n):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1],array[i-j] = array[i-j],array[i-j-1]
            else:
                break

    return array

print(insertion_sort(input)) # [1, 2, 4, 6, 9] 가 되어야 합니다!
print(insertion_sort2 (input)) # [1, 2, 4, 6, 9] 가 되어야 합니다!

# O(n^2) 하지만 break문이 있다. 최선의 경우 O(n)만큼 걸릴 수 있다.