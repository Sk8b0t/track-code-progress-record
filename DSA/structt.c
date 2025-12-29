#include <stdio.h>
#include <string.h>
struct emp
{
    char name[34];
    int id;
    float empScore;
};

int main()
{
    struct emp e1={"sayan",1,34.4};
    struct emp e2={"nayas",2,22.4};
    struct emp e3={"sia",3,99.4};
    printf("employee of the month goes to %s\n", e3.name);
    printf("The worst employee is %s with id %d and employee score %f", e2.name,e2.id,e2.empScore );
   

    return 0;
}
