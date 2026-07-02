#include<bits/stdc++.h>
using namespace std;
void inc(int &n1,int &n2){
    n1++;
    n2++;
}
void swap(int &a,int &b){
    int temp=a;
    a=b;
    b=temp;
}
int main(){
    int a=89,b=5;
    cout << a<<" "<<b<<endl;
    swap(a,b);
    cout << a<<" "<<b<<endl;

}