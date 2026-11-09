#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int H,W;
vector<vector<int>>dir={{1,0},{0,1},{-1,0},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};

void dfs(int i,int j,vector<vector<char>>&node,vector<vector<int>>&height){
    if(height[i][j]!=-1) return ;
    height[i][j]=1;
    for(auto &d:dir){
        int x=d[0]+i;
        int y=d[1]+j;
        if(x<0||y<0||x>=H||y>=W) continue;
        if(node[x][y]!=node[i][j]+1) continue;
        dfs(x,y,node,height);
        height[i][j]=max(height[i][j],height[x][y]+1);
    }


}

void solve(){
    int case_num=1;
   while((cin>>H>>W) && (H!=0||W!=0)){
   vector<vector<int>>height(H,vector<int>(W,-1));
   vector<vector<char>>node(H,vector<char>(W));
   for(int i=0;i<H;++i){
       for(int j=0;j<W;++j){
        cin>>node[i][j];
       }
   }
   int ans=0;
   for(int i=0;i<H;++i){
    for(int j=0;j<W;++j){
        if(node[i][j]=='A'){
             dfs(i,j,node,height);
             ans=max(ans,height[i][j]);
        }
    }
   }
   cout << "Case " << case_num++ << ": " << ans << "\n";
}
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}