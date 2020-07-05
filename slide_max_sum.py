# Find the maximum contigous sum of size 'k' given a list of integers of size 'n'


def slide_max_sum(nums, k):
  # We'll use the sliding window pattern
  window_sum = 0

  # First, compute the initial "window" sum
  for i in range(k):
    window_sum += nums[i]

  # init the max_sum as the window_sum
  max_sum = window_sum

  for i in range(k, len(nums)):
    window_sum = (window_sum + nums[i]) - nums[i - k]
    max_sum = max(window_sum, max_sum)

  return max_sum


print(slide_max_sum([50, 100, 34, 1, 6, 4, 35], 3))
