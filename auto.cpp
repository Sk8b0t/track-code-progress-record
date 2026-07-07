#include <bits/stdc++.h>;
using namespace std;
int main(){
    vector<pair<int,int>>v={{1,2},{2,3},{3,4}};
    vector<int>a={5,6,7,69,9};
    for(int &i:a){
        cout<<i<<endl;
    }

    for(pair<int,int> item:v) cout<<item.first<<" "<<item.second<<endl;
     for(auto item:v) cout<<item.first<<" "<<item.second<<endl;
    
}