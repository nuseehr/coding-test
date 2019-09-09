#include <iostream>

using namespace std;

int dp[12];

int main() {
    int testCases;
    cin >> testCases;
    
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    
    for (int i=4; i<11; i++) dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
    
    
    while (testCases--) {
        int N;
        cin >> N;
        cout << dp[N] << endl;
    }
}
