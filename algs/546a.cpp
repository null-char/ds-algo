// Link: https://codeforces.com/problemset/problem/546/A

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // k is the cost of the first banana
    // n is the initial amount of dollars he has
    // w is the number of available bananas in the shop
    int k, n, w;
    cin >> k >> n >> w;

    // The amount that is actually required to buy all w bananas;
    int required = 0;
    for (int i = 1; i <= w; i++) {
        // Each banana will cost i * k dollars i.e the cost of the banana increases based on
        // the number of bananas he buys.
        required += i * k;
    }

    // Borrow money if required exceeds initial
    int haveToBorrow = 0;
    if (required > n)
        haveToBorrow = required - n;

    cout << haveToBorrow << '\n';
}