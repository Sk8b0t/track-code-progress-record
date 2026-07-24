#include<bits/stdc++.h>
using namespace std;
using ll = long long;
void solve(){
    int n,q;
    cin>>n;
    vector<int>a(n);
    for(auto &itm:a){
        cin>>itm;
    }
    vector<int>pre(n+1,0);
    for(int i=1;i<=n;++i){
        pre[i]=pre[i-1]+a[i-1];
    }
    cin>>q;
    while(q--){
        int x;
        cin>>x;
        int low=1,high=n,mid;
        while(low<=high){
            mid=(low+high)/2;
            if(pre[mid]>=x) high=mid-1;
            else low=mid+1; 
        }
        cout<<high+1<<endl;
 
}

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}




