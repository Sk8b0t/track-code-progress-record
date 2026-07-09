class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
            int len=nums.size();
    for(int i=0;i<len;++i){
        nums.push_back(nums[i]);
    }
    vector<int>ind;
    stack<int> st;
    for(int i=0;i<nums.size();++i){
        while(!st.empty()&& nums[i]>nums[st.top()]){
            ind[st.top()]=i;
            st.pop();
        }
        st.push(i);
    }
    while(!st.empty()){
        ind[st.top()]=-1;
        st.pop();
    }
    vector<int> ans;
    for(int i=0;i<len;++i){
        if(ind[i]<0) ans.push_back(-1);
        else ans.push_back(nums[ind[i]]);
    }
    return ans;
        
    }
};
int main(){
    
}