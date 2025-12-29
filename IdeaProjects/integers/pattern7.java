package com.company;
//To print this pattern:-
//12341
//12321
//12321
//14321
//54321
public class pattern7 {

    public static void main(String[] args) {

        int m=4;
        String red="\u001B[31m",black_background="\u001B[40m";

        System.out.println(black_background);

         //from here
        for(int i=0;i<=3;i++) {
            for (int j =1; j<=m; j++) {
                System.out.print(red + j);
            }
              m--;
            for (int k = i + 1; k>0; k--) {
                System.out.print(red + k);
            }

            System.out.println();

        }
            //System.exit(18930);
        String a="v";
        System.out.println("\uf03F");
        }
    }

