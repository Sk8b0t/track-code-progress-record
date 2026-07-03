#include <bits/stdc++.h>
using namespace std;
const int N=1e7+10;
int hsh[N];
int main(){
    int n;
    int a[n];
    cin>>n;
    for(int i=0;i<n;++i){
        cin>>a[i];
        hsh[i]++;
    }
    int q;
    cin>>q;
    while(q--){
        int x;
        cin>>x;
        cout<<hsh[x]<<endl;
    }
}