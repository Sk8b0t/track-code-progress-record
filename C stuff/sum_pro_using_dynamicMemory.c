#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *ptr;
    ptr = (int *)malloc(4 * sizeof(int));

    for (int i = 0; i < 4; i++)
    {
        ptr[i] = i++;
    }

    int sum = 0, pro = 1;

    for (int i = 0; i < 4; i++)
    {
        sum += ptr[i];
    }

    free(ptr);
    ptr = (int *)calloc(4, sizeof(int));

    for (int i = 0; i < 4; i++)
    {
        pro *= ptr[i];
    }

    
    printf("%d %d\n", sum, pro);
    free(ptr);

    return 0;
}