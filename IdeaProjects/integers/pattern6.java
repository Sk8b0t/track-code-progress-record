package com.company;
//To print this pattern :-
//A
//A B
//A B C
//A B C D

public class pattern6 {
    public static void main(String[] args) {
        for(int i=64;i<68;i++){
            for(int j=64;j<=i;j++){
                System.out.print("\u001B[31m"+(char)(j+1)+" ");
            }
            System.out.println();
        }
    }
}
