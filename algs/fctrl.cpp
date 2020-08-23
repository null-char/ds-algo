// Link: https://www.spoj.com/problems/FCTRL/

#include <iostream>

// Definition and implementation of function Z(N) that takes in a number
// and calculates how many trailing zeroes N! would have.

/// Finds number of trailing zeroes of the factorial of the input integer n.
int findTrailingZeroes(int n) {
  int tz = 0;

  while (n >= 1) {
    n /= 5;
    tz += n;
  }

  return tz;
}

int main() {
  int T;
  scanf("%u", &T);

  for (auto i = 0; i < T; i++) {
    int n;
    scanf("%u", &n);
    printf("%u\n", findTrailingZeroes(n));
  }
}
