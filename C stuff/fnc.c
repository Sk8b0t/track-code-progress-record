#include <stdio.h>
int sum(int a, int b)
{
    return a + b;
}

int main()
{
    int num1, num2;
    printf("Enter 1st number :");
    scanf("%d", &num1);
    printf("Enter 2nd number: ");
    scanf("%d", &num2);
    printf("Sum: %d", sum(num1, num2));

    return 0;
}