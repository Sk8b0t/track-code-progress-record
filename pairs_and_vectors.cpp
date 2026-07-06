#include <bits/stdc++.h>
using namespace std;
int main(){
    pair<int,string> p={23,"njr"};
    cout<<p.first<<" "<<p.second<<endl;
    pair<int,string>&p1=p;
    p1.first=10;
    cout<<p.first<<endl;
    int a[]={1,2,3};
    int b[]={2,3,4};
    pair<int,int> p_arr[3];
    p_arr[0]={1,2};
    p_arr[1]={2,3};
    p_arr[2]={3,4};
    cout<<p_arr[0].first<<endl;
    swap(p_arr[0],p_arr[2]);
    for(int i=0;i<3;++i){
        cout<<p_arr[i].first<<" "<<p_arr[i].second<<endl;
    }


}