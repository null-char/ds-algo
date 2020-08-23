def epigram(s):
  # I'm guessing the algorithm will need to differentiate between uppercase and lowercase letters

  s_sum = 0
  vowels = 'aeiou'

  for x in s:
    if not x.isalpha():
      continue

    code = ord(x)

    if x.lower() in vowels:
      s_sum -= code
    else:
      s_sum += code

  return s_sum


print(
    epigram(
        "Dealing with failure is easy: Work hard to improve. Success is also easy to handle: You’ve solved the wrong problem. Work hard to improve."
    ))
