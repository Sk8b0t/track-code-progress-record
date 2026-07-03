#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,q;
        cin>>n>>q;
        int arr[n+10];
        for(int i=1;i<=n;++i){
            cin>>arr[i];
        }

        int f[n+10],b[n+10];
        f[0]=b[n+1]=0;
        for(int i=1;i<=n;i++){
                f[i]=__gcd(f[i-1],arr[i]);
        }
        for(int i=n;i>=1;--i){
                b[i]=__gcd(b[i+1],arr[i]);
            }
        
        while(q--){
            int l,r;
            cin>>l>>r;
            cout<<__gcd(f[l-1],b[r+1])<<endl;
    }
}
}

