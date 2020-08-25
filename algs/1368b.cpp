// Link: https://codeforces.com/contest/1368/problem/B

#include <bits/stdc++.h>
using namespace std;

int main() {
    string cfs = "codeforces";
    long long k, p, arr[10];
    cin >> k;

    p = 1;
    for (int i = 0; i < 10; i++) arr[i] = 1;

    while (p < k) {
        for (int i = 0; i < 10; i++) {
            p /= arr[i];
            arr[i]++;
            p *= arr[i];

            if (p >= k) {
                break;
            }
        }
    }

    for (int i = 0; i < 10; i++) {
        while (arr[i]--) {
            cout << cfs[i];
        }
    }
}