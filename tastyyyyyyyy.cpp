#include<bits/stdc++.h>
using namespace std;
using ll = long long;
bool pred(vector<ll>&a,int k,ll total_time){
    int cnt=1;
    ll time=0;
    for(auto &item:a){
        if(item>total_time) return false;
        if(time+item>total_time) {
            ++cnt;
            time=item;
    }
    else{
        time+=item;
    }
}
    return cnt<=k;
}
void solve(){
  int n,k;
  cin>>n>>k;
  vector<ll>a(n);
  ll total=0,max_ele=0;
  for(int i=0;i<n;++i){
    cin>>a[i];
    total+=a[i];
    max_ele=max(max_ele,a[i]);
  }
  ll lo=max_ele,hi=total,mid;
  while(lo<=hi){
    mid=(lo+hi)/2;
    if(pred(a,k,mid)) hi=mid-1;
    else lo=mid+1;
  }
  cout<<hi+1<<endl;

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){

    solve();
    }
    return 0;
}