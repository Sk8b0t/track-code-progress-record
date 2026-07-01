#include <bits/stdc++.h>
using namespace std;
int main(){
    // for(int i=0;i<=10;cout<<i++<<endl){

    // }
    for(int i=0;i<=10;++i){
        cout<<i<<endl;
    }
    int n;
    cout<<"Enter the value of n: ";
    cin>>n;
    for(int i=0;i<n+1;++i){
        for(int j=0;j<=i;++j){
            cout<<"*";
        }
        cout<<endl;
    }


}