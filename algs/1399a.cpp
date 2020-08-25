// Link: https://codeforces.com/problemset/problem/1399/A

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<vector<int>> inputVecs;

    // Number of test cases
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        // Length of test case array
        int n;
        cin >> n;
        vector<int> vec;

        for (int j = 0; j < n; j++) {
            int elem;
            cin >> elem;
            vec.push_back(elem);
        }

        inputVecs.push_back(vec);
    }

    // Process test cases
    for (vector<int> vec : inputVecs) {
        // Sort vec in ascending order
        sort(vec.begin(), vec.end());
        int R = 0;

        for (int i = 0; i < vec.size() - 1; i++) {
            if (abs(vec.at(i) - vec.at(i + 1)) > 1)
                R = 1;
        }

        auto ans = R == 0 ? "YES" : "NO";
        cout << ans << '\n';
    }
}