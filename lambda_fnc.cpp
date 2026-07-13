#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int>v={1,2,4,5,7,4,3};
    cout<<all_of(v.begin(),v.end(),[](int x){return x%2==0;});
}