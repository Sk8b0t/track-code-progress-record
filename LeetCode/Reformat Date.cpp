#include<bits/stdc++.h>
using namespace std;
string reformatDate(string date) {
    int n=date.size();
    string ans=date.substr(n-4)+"-";
    vector<string> mon={"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    string wtf=date.substr(n-8,3);
    int i=0;
    while(mon[i]!=wtf)
    ++i;
    ++i;
    if(i<10) ans+="0";
    ans+=to_string(i);
    ans+="-";
    i=0;
    string value="";
    while(date[i]>='0'&&date[i]<='9'){
        value+=date[i];
        ++i;
    }
    if(stoi(value)<10) value='0'+value;
    ans+=value; 
    return ans;
    }




  