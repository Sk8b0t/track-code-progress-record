#include <stdio.h>
#include <string.h>
//strcat() , strlen() , strcmp() , strrev(), strcpy()
void prnt(char str[])
{
    int i = 0;
    while (str[i] != '\0')
    {
        printf("%c", str[i]);
        i++;
    }
    printf("\n");
}

int main()
{
    // don't use scanf in strings bcoz it wont take whitespaces then (use gets fnc. instead)
    char n[] = {'s', 'a', 'y', 'a', 'n', '\0'};
    prnt(n);

    // most used
    char s[6] = "sayan";
    printf("%s\n", s);

    char str[34];
    gets(str);
    puts(str);


    char str1[]= "Sayan Vishwas";
    char str2[]= "Sia , pookie , cake1 , cake2 , jiggle , corporate girl";
    printf("length of str1 is %d\n" , strlen(str1));
    printf("length of str2 is %d\n" , strlen(str2));
    printf("The reverse of str1 is : %s\n" , strrev(str1));
    printf("The reverse of str2 is : %s\n" , strrev(str2));


    return 0;
}
