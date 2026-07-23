#include<bits/stdc++.h>
using namespace std;
using ll=long long;
const int N=1e5+10;
int n,c;
int pos[N];
bool preedicate(int dist){
    int lastpos=pos[0];
    int count=c-1;
    for(int i=0;i<n;++i){
        if(abs(lastpos-pos[i])>=dist){
            count--;
            lastpos=pos[i];
        }
        if(count==0) return true;
    
    }
    return  false;
}
void solve(){
  cin>>n>>c;
  for(int i=0;i<n;++i){
    cin>>pos[i];
  }
  sort(pos,pos+n);
  int l=1,h=pos[n-1]-pos[0],mid;

  while(l<=h){
    mid=(h+l)/2;
    if(preedicate(mid)) l=mid+1;
    else h=mid-1;
  }
  if(preedicate(h)) cout<<h<<"\n";
  else cout<<l<<"\n";


}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        solve();
    }

}