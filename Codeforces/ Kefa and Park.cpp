#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int ans=0;

void dfs(int vertex,int par,vector<vector<int>>&node,int cat_cnt,int m,vector<int>&a){
    if(a[vertex]==1) cat_cnt++;
    else cat_cnt=0;
    if(cat_cnt>m) return;

    bool leaf=true;
    for(auto &child:node[vertex]){
        if(child!=par){
            leaf=false;
            dfs(child,vertex,node,cat_cnt,m,a);
        }
    }
    if(leaf && vertex!=1) ans++;
}

void solve(){
    int n,m;
    cin>>n>>m;
    vector<int>a(n+1);
    for(int i=1;i<=n;++i) cin>>a[i];
    vector<vector<int>>node(n+1);
    for(int i=0;i<n-1;++i){
        int x,y;
        cin>>x>>y;
        node[x].push_back(y);
        node[y].push_back(x);
    }
    dfs(1,0,node,0,m,a);
    cout<<ans<<endl;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}