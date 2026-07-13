#include<bits/stdc++.h>
using namespace std;
int main(){
    // int arr[]={4,5,5,25,7,8};
    // int n=6;
    // sort(arr,arr+n);
    // for(auto itm:arr) cout<<itm<<" ";
    // cout<<endl;
    // int *ptr=lower_bound(arr,arr+n,6);
    // int *ptr1=upper_bound(arr,arr+n,7);
    // cout<<*ptr<<" "<<*ptr1<<endl;

    vector<int>v={4,5,5,25,7,8};
    sort(v.begin(),v.end());
    for(auto &itm: v) cout<<itm<<" ";
    cout<<endl;
    auto it=lower_bound(v.begin(),v.end(),5);
    if(it==v.end()) return 0;
    cout<<(*it)<<endl;

}
