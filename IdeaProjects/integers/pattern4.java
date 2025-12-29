package com.company;
//To print the following pattern :
//  a
//  a a
// a a a
//a a a a
public class pattern4 {
    public static void main(String[] args) {
        int m=5;
         String red="\033[1;91m",background_black="\u001B[40m",orange="\033[0m";
          System.out.println("\u001B[46m");
         System.out.println("\u001B[41m");

        for(int i=0;i<=5;i++){
            for(int k=m;k>0;k--) {
                System.out.print("  ");
            }
            for(int j=0;j<=i;j++){
                System.out.print(" ᓚᘏᗢ ");
            }
            m--;
            System.out.println();
        }


         System.out.println("\u001B[46m");
    }
}
