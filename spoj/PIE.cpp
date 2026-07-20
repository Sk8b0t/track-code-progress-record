#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int N = 10e6 + 9;
int n, f;
const double eps=1e-6;
vector<double> pievol;
bool predicate(double vol)
{
    int pieces = 0;
    for (auto &itm : pievol)
        pieces += (int)(itm / vol);
    return pieces>=f;
}

void solve()
{
    pievol.clear();
    cin >> n >> f;
    ++f;
    for (int i = 0; i < n; ++i)
    {
        double rad;
        cin >> rad;
        double pi = std::acos(-1.0);
        pievol.push_back(pi * rad * rad);
    }
    double l=0,h=*max_element(pievol.begin(),pievol.end()),mid;
    while(h-l>eps){
        mid=(h+l)/2;
        if(predicate(mid)) l=mid;
        else h=mid;
    }
    if(predicate(h)) cout<<fixed<<setprecision(4)<<h<<"\n";
    else cout<<fixed<<setprecision(4)<<l<<"\n";
    
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}