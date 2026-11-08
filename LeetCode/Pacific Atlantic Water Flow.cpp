#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int n,m;
vector<vector<int>>dir={{0,1},{0,-1},{1,0},{-1,0}};
void dfs(int i,int j, vector<vector<int>>&heights,vector<vector<bool>>&vis){
    vis[i][j]=true;
    for(auto &d:dir){
        int x=d[0]+i;
        int y=d[1]+j;
        if(x<0||y<0||x>=m||y>=n) continue;
        if(vis[x][y]) continue;
        if(heights[i][j]>heights[x][y]) continue;
        dfs(x,y,heights,vis);
    }
    
}
vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
    m=heights.size();
    n=heights[0].size();
    vector<vector<bool>>pacific(m,vector<bool>(n,false));
    vector<vector<bool>>atlantic(m,vector<bool>(n,false));

    for(int i=0;i<n;++i) dfs(0,i,heights,pacific);
    for(int i=0;i<m;++i) dfs(i,0,heights,pacific);
    for(int i=0;i<n;++i) dfs(m-1,0,heights,atlantic);
    for(int i=0;i<m;++i) dfs(0,n-1,heights,atlantic);

    vector<vector<int>>res;

    for(int i=0;i<m;++i){
        for(int j=0;j<n;++j){
            if(pacific[i][j]&&atlantic[i][j]) res.push_back({i,j});
        }
    }
return res;

}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}