// Link: https://codeforces.com/problemset/problem/617/A

#include <bits/stdc++.h>
using namespace std;

// The max step the elephant can take
const int MAX_STEP = 5;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // Coordinate of friend's house
    int x;
    cin >> x;
    int steps = 0;
    int ex = 0;

    // Take 5 steps each time as long as we don't overshoot. If there's a possibility of overshooting
    // then we move x - ex positions forward.
    while (ex != x) {
        if (ex + MAX_STEP <= x) {
            ex += MAX_STEP;
        } else {
            ex += x - ex;
        }
        steps++;
    }

    cout << steps << '\n';
}
