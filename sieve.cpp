#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int N=1e7+10;
vector<bool>isPrime(N,1);
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    isPrime[0]=isPrime[1]=false;
    for(int i=2;i<N;++i){
        if(isPrime[i]){
            for(int j=2*i;j<N;j+=i){
                isPrime[j]=false;
            }
        }
        
    }
    for(int i=1;i<30;++i){
        cout<<isPrime[i]<<endl;
    }

    return 0;
}