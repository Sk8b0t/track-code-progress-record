#include<bits/stdc++.h>
using namespace std;
const int N=1e5+10;
int a[N];
int pre[N];
int main(){
  int n;
  cin>>n;
  for(int i=1;i<=n;++i){
    cin>>a[i];
    pre[i]=pre[i-1]+a[i];
  }       
  int q;
  cin>>q;
  while(q--){
    int l,r;
    cin >>l>>r;
    cout<<pre[r]-pre[l-1]<<endl;
  }
 
}