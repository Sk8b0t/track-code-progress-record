#include <bits/stdc++.h>
using namespace std;
const int N=1e3;
int arr[N][N];
long long pre[N][N];
int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;++i){
        for(int j=1;j<=n;++j){
            cin>>arr[i][j];
            pre[i][j]=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]+arr[i][j]
        }
    int q;
    cin>>q;
    while(q--){
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        cout<<pre[c][d]-pre[a-1][d]-pre[c][b-1]+pre[a-1][b-1]<<endl;
    }
    }


}