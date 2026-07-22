#include<bits/stdc++.h>
using namespace std;
using ll = long long;

bool pred(vector<int>pre,int dist,int k,int n){
    int k_cnt=0;
    for(int i=1;i<=n;++i){
        k_cnt=max(k_cnt,(pre[i]+dist-1)/dist);
    }
    return k_cnt<=k; 
}

void solve(){
  int n,k;
  cin>>n>>k;
  vector<int>a(n);
  for(auto &itm:a) cin>>itm;
  vector<int>pre(n+1,0);
  for(int i=1;i<=a.size();++i)
       pre[i]=pre[i-1]+a[i];

  int lo=pre[1],hi=pre[n],mid;
  while(lo<=hi){
    mid=(lo+hi)/2;
    if(pred(pre,mid,k,n)) lo=mid;
    else hi=mid-1;
  }
  cout<<hi<<"\n";
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}