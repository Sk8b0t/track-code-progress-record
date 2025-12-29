package com.company;

public class pattern8 {
    public static void main(String[] args) {
        String red="\u001B[31m",blackBg="\u001B[40m";
        System.out.println(blackBg);
        for (int i = 1; i <= 5; i++) {
            if (i % 2 == 0) {
                for (int j = 1; j <= i; ++j) {
                    System.out.print(red+" 0\t");
                }
            } else {
                for (int j = 1; j <= i; ++j) {
                    System.out.print(red+" 1\t");
                }

            }
            System.out.println();

        }
    }
}
