def odd_fib():
  # The current fibonacci number will be the sum of p1 and p2
  p2, p1 = 0, 1
  # We'll start our odd sum at 1 as p1 is odd
  odd_sum = 1

  while p1 < 10000:
    # Get current sequence number
    cur = p1 + p2

    # Check if odd. If so, add it to our odd_sum
    if cur % 2 != 0:
      odd_sum += cur

    # Update p1 and p2
    p2 = p1
    p1 = cur

  return odd_sum


print(odd_fib())