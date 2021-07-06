input = [4, 6, 2, 9, 1]
input2 = [4, 6, 2, 9, 1]

def bubble_sort(array):
    n = len(array)
    while True:
        swap = False # 이미 정렬되어 있는 리스트는 정렬을 수행할 필요가 없기 때문.
        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swap = True
        if not swap:
            break
        n -= 1
    return

def bubble_sort_2(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return

bubble_sort(input) # O(n^2)
bubble_sort_2(input2) # O(n^2)
print(input)
print(input2)