#include <stdio.h>
int main()
{
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    if (age < 18)
    {
        printf("You cannot drive");
    }
    else if (age >= 18 && age <= 24)
    {
        printf("You can drive but drive carefully ");
    }
    else
    {
        printf("You can drive");
    }

    // Excersie - learn switch statement

    return 0;
}