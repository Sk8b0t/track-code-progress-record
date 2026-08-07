#include<bits/stdc++.h>
using namespace std;
using ll = long long;

  vector<vector<int>> subsets(vector<int>& nums) {
       vector<vector<int>>ans;
       int len=1<<nums.size();
       for(int i=0;i<len;++i){
        vector<int>sub;
        for(int j=0;j<nums.size();++j){
            if((i&(1<<j))==1) sub.push_back(nums[j]);
        }
        ans.push_back(sub);

       }
       return ans;
    }