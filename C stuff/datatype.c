#include <stdio.h>
 int main(){
    int a=69;
    long l=2345;
    unsigned int d=8;
    unsigned short s=1;
    const int i=0; // "i" is read only variable

    float b=6.9; // 6 defcimal precision
    double s1=1;  //15 decimal precison
    long double ld=0.3246545654; //19 decimal precison

     char c ='S';

    // %d - integer
    // %f - float
    //%c  - char
    printf("The integer number is : %d\n" ,a);
    printf("the float number is %f\n", b);
    printf("The character is %c", c);

    printf("The size of int is %d\n", sizeof(int));
    printf("The size of short is %d\n", sizeof(short));
    printf("The size of long is %d\n", sizeof(long));
    printf("The size of unsigned int is %d\n", sizeof(unsigned int));
    printf("The size of long double is %d\n", sizeof(long double));







    return 0;
 }