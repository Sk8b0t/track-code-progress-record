package com.company;

import java.sql.SQLOutput;

public class christmas_tree {
    public static void main(String[] args) {
        //To print this output:
//       ★
//       s
//      s h
//     s h e
//    s h e e
//   s h e e t
//  s h e e t a
// s h e e t a l
//      ||


        java.util.Scanner in=new java.util.Scanner(System.in);

//        System.out.print("Enter your name !! : ");
//           String n=in.nextLine();
         String n = "SHEETAL";
        int len = n.length() , print = 0;

//To put the star in position
           int m=len/2;
        {
            for (int k = 1; k <= m; k++)
                System.out.print("  ");
            System.out.println("\u001B[33m" + " " + (char) 9733);

        }

        {
            //the main logic for christmas tree
            for (int i = 0; i <n.length(); i++) {
                for (int k = len - i; k > 0; k--)
                    System.out.print(" ");
                for (int j = 0; j <= print; j++)
                    System.out.print(n.charAt(j) + " ");
                System.out.println();
                print++;
            }
        }

        {
            //for the bark of the tree
            for (int k = 1; k <= m; k++) {
                System.out.print("  ");

            }
            System.out.println("\u001B[30m" + "||");
//end of the program
        }

    }
}
