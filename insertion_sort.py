# Given an array of n elements, sort it in ascending order using insertion sort.


def insertion_sort(arr):
  for i in range(1, len(arr)):
    for j in range(i, 0, -1):
      if arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]

  return arr


print(insertion_sort([5, 5, 3, 3, 1]))