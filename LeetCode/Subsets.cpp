#include<bits/stdc++.h>
using namespace std;

vector<vector<int>>ans;  
void gen(vector<int>&sub,int i,vector<int>v){
      if(i==v.size()){
        ans.push_back(sub);
        return;
    }
    sub.push_back(v[i]);
    gen(sub,i+1,v);
    sub.pop_back();
    gen(sub,i+1,v);

}
vector<vector<int>> subsets(vector<int>& nums) {
    vector<int>sub;
    int i=0;
    gen(sub,i,nums);
    return ans;
}

int main(){
    vector<int>x={1,2,3};
    for(auto &item:subsets(x)){
        for(auto &ele:item) cout<<ele<<" ";
        cout<<endl;
    }
}