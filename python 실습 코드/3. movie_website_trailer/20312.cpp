#include <bits/stdc++.h>
using namespace std;
/*
    알고리즘 : dp
*/
#define MAX 500000
const int MOD = 1e9 + 7;
int n, arr[MAX], prefix[MAX];

int main(int argc, char* argv[]){
    cin >> n;
    int t = 1; arr[0] = 1;
    for(int i = 1 ; i < n ; i++){
        cin >> arr[i];
        t = (t * arr[i]) % MOD;
        prefix[i] = (prefix[i - 1] + t) % MOD; 
    }
    //모든 i, j에 대해 빠른 정도를 더한값을 구한다.
    //처음에 sum을 구해놓고 거기서 부터 값을 구해나간다.
    t = 1;
    int answer = 0;
    for(int i = 1 ; i < n ; i++){
        answer += (prefix[n - 1] - prefix[i - 1]) / t;
        t *= arr[i];
    }

    cout << answer << endl;
}