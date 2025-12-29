#include <stdio.h>
#include <string.h>
// \0 ka matlab "NULL" hota h
void points()
{
    int a = 45;
    int *ptr=   NULL;
    ptr = &a;
    *ptr = 677;
    printf("%d\n", a);
}

struct Books{

    char name[50];
    char auth[50];
    int p;
}book;

void prntstruct_book(struct Books bk){
    printf("The book name is %s\n", bk.name);
    printf("The author name is %s\n", bk.auth);
    printf("The price of the book is $%d\n", bk.p);

}


void stringop(){
    char s[3]= {'m', 'y','\0'};
    char str1[110], str2[120];

    //String functions : strcat() , strcpy() , strcmp()
    
    strcpy(str1 , s);
    printf("%s\n", str1);

    strcpy(str1, "Sayan");
    strcpy(str2, "Vishwas");

    printf("str1 : %s\n", str1);
    printf("str 2: %s\n", str2);

    strcat(str1 , str2);
    printf("%s" ,str1);

}
  
int main()
{
    int arr[10] = {0, 1, 2, 3, 4, 5};
    for (int i = 0; i < 6; i++)
    {

        printf("the value in the array in the %d index is %d\n", i, arr[i]);
    }

    points();
    stringop();

    struct Books bk1, bk2;
    strcpy(bk1.name, "Neymar the magician!!");
    strcpy(bk1.auth , "sayan");
    bk1.p = 4444;
    prntstruct_book(bk1);


    return 0;
}
