#include<bits/stdc++.h>
using namespace std;
using ll = long long;

void printBinary(int n){
    string s="";
    while(n>=1){
        s+=to_string(n%2);
        n=n>>1;
    }
    
    reverse(s.begin(),s.end());
    cout<<s<<"\n";
}

//to count no. of set bits
int count_set_bits(int num){
    int cnt=0;
    while(num>=1){
        cnt+=num&1;
        num=num>>1;
    }
    return cnt;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    printBinary(13);
    cout<<count_set_bits(13);

    return 0;
}