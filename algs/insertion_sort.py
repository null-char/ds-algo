# Given an array of n elements, sort it in ascending order using insertion sort.

# A quick explanation: This is very similar to how you sort playing cards. Every card on the table
# (faced down) is unsorted. Every card on your hand is sorted. This is the basic intuition behind
# insertion sort. As the name implies, we pick a key element and decide where to appropriately put it.


def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i - 1
    key = arr[i]

    while (j >= 0) and (arr[j] > key):
      arr[j + 1], arr[j] = arr[j], arr[j + 1]
      j -= 1
    arr[j + 1] = key

  return arr


print(insertion_sort([10, 7, 3, 6]))

# A quick proof using loop invariants (this is essentially just mathematical induction):
# We will only consider the outer for loop for the loop invariant.
# Initially, we have a subarray arr[0..1] which is obviously sorted since it consists of only
# one element. Notice that if this invariant holds true before an iteration and before the next
# iteration, we can effectively prove that the algorithm is correct.
# We can assume that before an iteration, arr[0..j] is sorted. Before the next iteration, we then
# appropriately place the key (arr[i]) into it's appropriate position, thus the invariant
# still holds true.
# Now, once the loop terminates, we have i = n + 1 (where n is the length of arr). We know from our
# previous assumption that arr[0..j] is sorted. Hence we simply substitute for j and we have thus proven
# that arr[1..n] is sorted. Since this "subarray" represents the entire array, we conclude that
# the algorithm has correctly sorted the entire array.