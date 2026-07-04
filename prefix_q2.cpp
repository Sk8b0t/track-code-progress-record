#include <bits/stdc++.h>
using namespace std;
const int N=10e7+10;
long long int arr[N];
long long int pre[N];
int main(){
    int n,q;
    cin>>n>>q;
    while(q--){
        int a,b,k;
        cin>>a>>b>>k;
        arr[a]+=k;
        arr[b+1]-=k;
    }
    for(int i=1;i<=n;++i){
        pre[i]=pre[i-1]+arr[i];
    }


     long long int mx =-1;
    for(int i=1;i<=n;++i){
        if (mx<pre[i]){
            mx=pre[i];
        }
    }
    cout<<mx<<endl;;

}
