#include <stdio.h>
#include <stdlib.h>
struct CstmArr
{
    int t_size;
    int u_size;
    int *ptr;
};

void initialize(struct CstmArr *a, int t, int u)
{
    a->u_size = u;
    a->t_size = t;
    a->ptr = (int *)malloc(t * sizeof(int));
}
void set(struct CstmArr *a)
{
    for (int i = 0; i < a->u_size; i++)
    {
        (a->ptr)[i] = i+69;
    }
    for (int i = 0; i < a->u_size; i++)
    {
        printf("The employee id at %d index is %d\n", i, (a->ptr)[i]);
    }
    free(a->ptr);
}
int main(){
    struct CstmArr empidArr;
    initialize(&empidArr,200,11);
    set(&empidArr);
    return 0;
}
