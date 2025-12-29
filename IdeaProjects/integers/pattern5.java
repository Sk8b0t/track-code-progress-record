package com.company;

//To print this pattern:
//     1
//    1 1
//   1 2 1
//  1 3 3 1
// 1 4 6 4 1

public class pattern5 {

    public static void main(String[] args) {

        String red="\033[1;91m",background_black="\u001B[40m",orange="\033[0m";
         System.out.println("\u001B[41m");

        int r;
        for (int i=1,m=5;i<=14641;i*=11,m--) {
            for (int k = m; k > 0; k--) {
                System.out.print(background_black+" ");
            }
            for (int j = i; j > 0; j/= 10) {
                r = j % 10;
                System.out.print(red+ r + " ");
            }
            System.out.println();
            

        }
        System.out.println("\u001B[41m");

            }
        }
