# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of
# both strings s and p will not be larger than 20,100.
# The order of output does not matter.


def find_all_anagrams(s, p):
  # If string p is larger in length than string s, then no anagrams will be found.
  if len(p) > len(s):
    return []

  dict_p = {}
  word_size = len(p)

  for ch in p:
    dict_p[ch] = dict_p.get(ch, 0) + 1

  l, r = 0, 0
  required = len(dict_p)
  formed = 0
  window_dict = {}
  out = []

  while r < len(s):
    rchar = s[r]

    if dict_p.get(rchar, None):
      window_dict[rchar] = window_dict.get(rchar, 0) + 1

      if dict_p[rchar] == window_dict[rchar]:
        formed += 1
    r += 1

    while formed == required:
      if r - l == word_size:
        out.append(l)

      lchar = s[l]
      if window_dict.get(lchar, None):
        window_dict[lchar] -= 1

        if window_dict[lchar] < dict_p[lchar]:
          formed -= 1

      l += 1

  return out


print(find_all_anagrams("cbaebabacd", "abc"))