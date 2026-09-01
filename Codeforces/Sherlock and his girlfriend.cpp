#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int N=1e5+5;
int hsh[N];
int hp[N];

vector<int>distinctPF(int x){
    vector<int>ans;
    while(x>1){
        int pf=hp[x];
        while(x%pf==0)x/=pf;
        ans.push_back(pf);
    }
    return ans;
}

void solve(){
    for(int i=2;i<N;++i){
        if(hp[i]==0){
            for(int j=i;j<N;j+=i){
                hp[j]=i;
            }
        }
    }
    int n;
    cin>>n;
    vector<int>a(n);
    for(int i=0;i<n;++i) a[i]=i+2;
    vector<int>ans(n,1);
    int cnt=0;
    for(int i=0;i<n;++i){
        if(distinctPF(a[i]).size()==1 && distinctPF(a[i])[0]==a[i]) continue;
        else ans[i]=2;

    }
    if(n>2) cout<<2<<endl;
    else cout<<1<<endl;

    for(auto &itm:ans) cout<<itm<<" ";
    cout<<endl;


}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

#ifndef ONLINE_JUDGE
    freopen("inputf.in", "r", stdin);
    freopen("outputf.out", "w", stdout);
#endif

    solve();
    return 0;
}