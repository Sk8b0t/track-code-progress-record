package com.company;
/*
To print this pattern
15	14	13	12	11
10	9	8	7
6	5	4
3	2
1

1
2	3
4	5	6
7	8	9	10
11	12	13	14	15

*/
public class pattern3 {
    public static void main(String[] args) {
        int i, j, p = 16;
        for (i = 5; i > 0; i--) {
            for (j = i; j > 0; j--) {
                p--;
                System.out.print(p + "\t");
            }
            System.out.println();
        }
        p=0;
            for(i=1;i<=6;i++){
                for (j=1;j<i;j++) {
                    p++;
                    System.out.print(p+ "\t");
                }
                System.out.println();
            }

        }
    }

