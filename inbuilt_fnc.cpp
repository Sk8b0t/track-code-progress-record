#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<int>v={1,2,5,45,5,6,7};
    int min=*min_element(v.begin(),v.end());
    int max=*max_element(v.begin(),v.end());
    int sum=accumulate(v.begin(),v.end(),0);
    int ct=count(v.begin(),v.end(),5);
    cout<<ct<<endl;
    int element=*find(v.begin(),v.end(),4);
    cout<<element;
    reverse(v.begin(),v.end());




}