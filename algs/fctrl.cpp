// Link: https://www.spoj.com/problems/FCTRL/

#include <iostream>

// Definition and implementation of function Z(N) that takes in a number
// and calculates how many trailing zeroes N! would have.

/// Finds number of trailing zeroes of the factorial of the input integer n.
int findTrailingZeroes(int n)
{
    int tz = 0;

    // The intuition here is to find the number of multiples of 5 that composes
    // n!. The multiples of 2 will be in far greater amount so we can instead
    // focus on finding multiples of 5. For some number x, the number of trailing
    // zeroes is described by the number of times x can be exactly divided by 10.
    while (n >= 1)
    {
        n /= 5;
        tz += n;
    }

    return tz;
}

int main()
{
    int T;
    scanf("%u", &T);

    for (auto i = 0; i < T; i++)
    {
        int n;
        scanf("%u", &n);
        printf("%u\n", findTrailingZeroes(n));
    }
}