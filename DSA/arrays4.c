#include <stdio.h>
int insert(int arr[], int ind, int e, int size)
{
    if(size!=0 && ind>=0 && ind<size){
    for (int i = size - 1; i >= ind; i--)
    {
        arr[i + 1] = arr[i];
    }
    arr[ind] = e;
}
else{
    return 0;
}
}
void dis(int a[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", a[i]);
    }

    printf("\n");
}
int del(int arr[], int ind, int size)
{
    if (size != 0 && ind >= 0 && ind < size)
    {
        for (int i = ind; i < size - 1; i++)
        {
            arr[i] = arr[i + 1];
        }
    }
    else
    {
        return 0;
    }
}

int main()
{

    int arr[100] = {1, 4, 5, 7, 8, 9};
    int size = 6;
    dis(arr, size);
    insert(arr, 1, 69, size);
    dis(arr, size);
    del(arr, 1, size);
    dis(arr, size);
    return 0;
}