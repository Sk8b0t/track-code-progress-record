#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int N=10e6+10;
ll trees[N];
ll m,n;

bool predicate(int h){
    ll wood=0;
    for(int i=0;i<n;++i){
        if(trees[i]>=h)
            wood+=(trees[i]-h);
    }
    return wood>=m;

}
void solve(){
    cin>>n>>m;
    for(int i=0;i<n;++i){
        cin>>trees[i];
    }
    ll low=0,high=10e8,mid;
    while(high-low>1){
        mid=(high+low)/2;
        if(predicate(mid)) low=mid;
        else high=mid-1;
    }
    if(predicate(high)) cout<<high<<"\n";
    else cout<<low<<"\n";



}
int main(){
     ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    
}