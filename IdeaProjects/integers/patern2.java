package com.company;
/* To print this pattern:-
15	14	13	12	11
10	9	8	7
6	5	4
3	2
1
*/
public class patern2 {
    public static void main(String[] args) {
        int i, j, p = 16;
        for (i=5; i>0;i--) {
            for (j=i;j>0;j--) {
                p--;
                System.out.print(p + "\t");
            }
            System.out.println();
        }
    }
}
