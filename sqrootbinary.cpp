#include<bits/stdc++.h>
using namespace std;
int main(){
    double x;
    cin>>x;
    double eps=10e-9;
    double low=1,hi=x,mid;
    while(hi-low>eps){
        mid=(hi+low)/2;
        if(mid*mid<x) low=mid;
        else hi=mid;
    }
    cout<<low;
    
}