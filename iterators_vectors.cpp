#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<int>v={5,6,7,69,9};
    for(int i=0;i<v.size();++i){
        cout<<v[i]<<" ";
    }
    cout<<endl;
    vector<int>::iterator it=v.begin();
    for(it=v.begin();it!=v.end();++it){
        cout<<*it<<endl;
    }
    vector<pair<int,int>> a={{1,2},{2,3},{3,4}};
    vector<pair<int,int>>::iterator i;
    for(i=a.begin();i!=a.end();++i){
        cout<< (*i).first<<" "<<(*i).second<<endl;
        //or
        cout<< i->first<<" "<<i->second<<endl;
    }
        





    }
}