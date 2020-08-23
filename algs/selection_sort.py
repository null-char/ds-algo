def selection_sort(arr):
  for i in range(len(arr) - 1):
    k = i

    for j in range(i, len(arr)):
      if arr[j] < arr[k]:
        k = j

    arr[i], arr[k] = arr[k], arr[i]

  return arr


print(selection_sort([10, 9, 5, 3, 1]))