#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N=1e6+10;
vector<bool>tprime(N,1);
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<bool>isPrime(N,1);
    isPrime[0]=isPrime[1]=false;
    for(int i=2;i<N;++i){
        if(isPrime[i]){
            for(int j=2*i;j<N;j+=i){
                isPrime[j]=false;
            }
        }
    }
    int n;
    cin>>n;
    vector<ll>x(n);
    for(auto &itm:x) cin>>itm;
    for(auto &itm:x){
        ll sq=sqrt(itm);
        if(sq*sq==itm && isPrime[sq]) cout<<"YES"<<"\n";
        else cout<<"NO"<<"\n";
        
    }

    return 0;
}