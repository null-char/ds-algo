def is_num_palindrome(num):
  reverse = 0
  temp = num

  while temp > 0:
    last_digit = temp % 10
    reverse = reverse * 10 + last_digit
    temp = temp // 10

  return num == reverse


p = []

# Generate all numeric palindromes less than 10,000
for n in range(1, 10000):
  if is_num_palindrome(n):
    p.append(n)

print(sum(p))