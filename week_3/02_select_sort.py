input = [4, 6, 2, 9, 1]

def select_sort(array):
  n = len(array)
  for i in range(n-1):
    min_value = i
    for j in range(i+1,n):
      if array[min_value] > array[j]:
        min_value = j
    array[i],array[min_value] = array[min_value],array[i]
  return array


def selection_sort(array):
  n = len(array)
  for i in range(n - 1):
    min_index = i
    for j in range(n - i):
      if array[min_index] > array[i+j]:
        min_index = i+j
    array[min_index],array[i] = array[i],array[min_index]
  return array


print(select_sort(input))
print(selection_sort(input))

# O(n^2)의 시간 복잡도