# Given a string S and a string T, find the minimum window in S
# which will contain all the characters in T in complexity O(n).


def min_window_substring(s, t):
  dict_t = {}

  for ch in t:
    dict_t[ch] = dict_t.get(ch, 0) + 1

  begin, end = 0, 0
  # Simply the number of unique characters in T
  required = len(dict_t)
  # Number of unique characters of T found in our window string
  formed = 0
  ans = ''
  # We'l init the min answer length to len(s) + 1 in case S and T are equal
  min_len = len(s) + 1

  window_dict = {}

  while end < len(s):
    endchar = s[end]

    if dict_t.get(endchar, None):
      window_dict[endchar] = window_dict.get(endchar, 0) + 1

      if dict_t[endchar] == window_dict[endchar]:
        formed += 1

    end += 1

    while formed == required:
      if end - begin < min_len:
        min_len = end - begin
        ans = s[begin:end]

      beginchar = s[begin]

      if window_dict.get(beginchar, None):
        # We'll be excluding this char in the next loop so decrement its frequency
        window_dict[beginchar] -= 1

        # Checks to see if the window is out of sync. If it is, then we no longer have
        # a valid substring
        if window_dict[beginchar] < dict_t[beginchar]:
          formed -= 1

      begin += 1

  return ans


print(min_window_substring("ADOBECODEBANC", "ABC"))