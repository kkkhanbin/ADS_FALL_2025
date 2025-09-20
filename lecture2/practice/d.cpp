#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    map<int, int> frequencies;

    int max_f = 0;
    for (int i = 0; i < n; i++) {
        int cur;
        cin >> cur;

        if (frequencies.find(cur) != frequencies.end()) {
            frequencies[cur]++;
            if (frequencies[cur] > max_f) {
                max_f = frequencies[cur];
            }

        } else {
            frequencies[cur] = 1;
            if (frequencies[cur] > max_f) {
                max_f = frequencies[cur];
            }
        }
    }

    // cout << "MAX_F - " << max_f << endl;

    vector<int> maxes;
    for (auto it = frequencies.begin(); it != frequencies.end(); ++it) {

        // cout << it -> first << " " << it -> second << endl;

        if (it -> second == max_f) {
            maxes.push_back(it -> first);
        }
    }

    sort(begin(maxes), end(maxes));

    for (int i = maxes.size() - 1; i >= 0; i--) {
        cout << maxes[i] << " ";
    }
}