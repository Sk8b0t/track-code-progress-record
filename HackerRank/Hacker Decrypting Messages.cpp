#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int N=1e6+4;
int hp[N];
bool canRemove[N];
int hsh[N];

vector<int>distinctPF(int x){
    vector<int>ans;
    while(x>1){
        int pf=hp[x];
        while(x%pf==0) x/=pf;
        ans.push_back(pf);
    }
    return ans;
}

void solve(){

    for(int i=2;i<N;++i){
        if(hp[i]==0){
            for(int j=i;j<N;j+=i) hp[j]=i;
        }
    }

    int n,q;
    cin>>n>>q;
    vector<ll>a(n);
    for(auto &itm:a){
        cin>>itm;
        hsh[itm]=1;
    }
    for(int i=2;i<N;++i){
        if(hsh[i]==1){
            for(ll j=i;j<N;j*=i) canRemove[j]=true;
        }
    }
    while(q--){
        int x;
        cin>>x;
        vector<int>pf=distinctPF(x);
        bool isPossible=false;
        for(int i=0;i<pf.size();++i){
            for(int j=i;j<pf.size();++j){
                int pro=pf[i]*pf[j];
                if(i==j && x%pro!=0) continue;
                int toRemove=x/pro;
                if(canRemove[toRemove]|| toRemove==1){
                    isPossible=true;
                    break;
                }
            }
            if(isPossible) break;
        }
        cout<<(isPossible?"YES\n":"NO\n");

    }

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