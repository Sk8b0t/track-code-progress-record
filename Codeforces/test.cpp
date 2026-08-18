    #include<bits/stdc++.h>
    using namespace std;
    using ll = long long;

    bool pred(vector<ll>&a,ll mid,ll x){
        ll tw=0;
        for(auto &itm:a){
            tw+=max(0LL,mid-itm);
            if(tw>x) return false;
        }
        return (tw<=x);
    }

    void solve(){
        int t;
        cin>>t;
        while(t--){
            ll n,x;
            cin>>n>>x;
            vector<ll>a(n);
            for(auto &itm:a) cin>>itm;
            ll l=1,r=2e9+9,mid;
            while(r>=l){
                mid=(r+l)/2;
                if(pred(a,mid,x))
                    l=mid+1;
                else
                r=mid-1;
            }
            cout<<r<<endl;
        }

    }

    int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        solve();
        return 0;
    }