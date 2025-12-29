#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *ptr;
    int s;
    printf("Enter the size of the array:");
    scanf("%d", &s);
    ptr = (int *)calloc(s, sizeof(int));

    for (int i = 0; i < s; i++){
        printf("Enter the integer at %d index:", i);
        scanf("%d", &ptr[i]);
    }

    for (int i = 0; i < s; i++){
        printf("integer at %d index: %d\n", i, ptr[i]);
    }
    int n;
    printf("Enter the new size of array");
    scanf("%d", &n);
    ptr= (int*)realloc(ptr, n*sizeof(int));

     for (int i = 0; i < n; i++){
        printf("Enter the integer at %d new index:", i);
        scanf("%d", &ptr[i]);
    }

    for (int i = 0; i < n; i++){
        printf("integer at %d new index: %d\n", i, ptr[i]);
    }


    return 0;
}