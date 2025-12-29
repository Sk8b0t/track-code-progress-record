#include<stdio.h>

void insert(int arr[],int ind,int ele,int size) {
    for (int i=size-1;i>=ind;i--) {
        arr[i+1]=arr[i];

    }
    arr[ind]=ele;
}

void delete(int arr[],int ind,int size) {
for (int i=ind;i<size-1;i++) {
    arr[i]=arr[i+1];
}}

void show(int arr[],int size) {
    for (int i=0;i<size;i++) {
        printf("%d ",arr[i]);
    }
    printf("\n");
}
int main() {
    int arr[100]={1,2,3,4,5};
    show(arr,5);
    insert(arr,1,69,5);
    show(arr,6);
    delete(arr,1,6);
    show(arr,5);

    return 0;
}
